import os
import sys
import re
import json
import logging
import argparse
import signal
import shutil
import tempfile
import zipfile
import tarfile
import gzip
import mimetypes
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

# 尝试导入 textract，如果失败则优雅降级
try:
    import textract
    TEXTRACT_AVAILABLE = True
except ImportError:
    TEXTRACT_AVAILABLE = False

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class CreditCardScanner:
    def __init__(self, root_path, ignore_list=None, exclude_exts=None, mask=False, max_depth=3, threads=4):
        self.root_path = root_path
        self.ignore_list = set(ignore_list) if ignore_list else set()
        self.exclude_exts = set(e.lower() for e in exclude_exts) if exclude_exts else set()
        self.mask_enabled = mask
        self.max_archive_depth = max_depth
        self.threads = threads
        self.results = []
        self.total_files = 0
        self.matches_found = 0
        self.abort_signal = False
        
        # 预编译正则，提升性能
        # 匹配主要卡组织格式 (简单的 \d{13,16} 误报太高)
        self.card_pattern = re.compile(r'\b(?:\d[ -]*?){13,16}\b')

    def luhn_check(self, card_number):
        """Luhn 算法校验"""
        digits = [int(c) for c in card_number if c.isdigit()]
        checksum = 0
        reverse_digits = digits[::-1]
        for i, digit in enumerate(reverse_digits):
            if i % 2 == 1:
                digit *= 2
                if digit > 9:
                    digit -= 9
            checksum += digit
        return checksum % 10 == 0

    def is_false_positive(self, clean_number):
        """过滤常见误报"""
        # 1. 排除全是一个数字的情况 (如 1111...)
        if len(set(clean_number)) == 1:
            return True
        # 2. 排除顺序数字 (如 123456...)
        if clean_number in "01234567890123456789":
            return True
        return False

    def get_card_type(self, number):
        """识别卡组织"""
        n = number
        if n.startswith('4') and len(n) in (13, 16): return 'VISA'
        if 51 <= int(n[:2]) <= 55 and len(n) == 16: return 'MasterCard'
        if n[:2] in ('34', '37') and len(n) == 15: return 'AMEX'
        if n.startswith('6011') and len(n) == 16: return 'Discover'
        # 可以根据需要添加更多规则
        return 'Unknown'

    def mask_card(self, number):
        """脱敏处理"""
        clean = re.sub(r'\D', '', number)
        if len(clean) < 10: return number
        return f"{clean[:4]}{'*' * (len(clean) - 8)}{clean[-4:]}"

    def extract_text(self, file_path):
        """提取文本内容，根据文件类型分发"""
        try:
            # 1. 尝试作为普通文本读取
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read()
        except Exception:
            # 2. 如果是二进制或特殊格式，尝试使用 textract (如果安装了)
            if TEXTRACT_AVAILABLE:
                try:
                    return textract.process(file_path).decode('utf-8', errors='ignore')
                except Exception:
                    pass
            return ""

    def process_content(self, text, file_path, archive_chain=None):
        """核心扫描逻辑"""
        if not text: return

        path_display = f"{' -> '.join(archive_chain)} -> {os.path.basename(file_path)}" if archive_chain else file_path
        
        for line_idx, line in enumerate(text.splitlines(), 1):
            for match in self.card_pattern.finditer(line):
                raw_card = match.group()
                clean_card = re.sub(r'\D', '', raw_card)

                if (13 <= len(clean_card) <= 16 and 
                    self.luhn_check(clean_card) and 
                    not self.is_false_positive(clean_card) and
                    clean_card not in self.ignore_list):
                    
                    card_type = self.get_card_type(clean_card)
                    final_card = self.mask_card(raw_card) if self.mask_enabled else raw_card
                    
                    # 记录结果
                    result = {
                        "file": path_display,
                        "line": line_idx,
                        "type": card_type,
                        "match": final_card,
                        "context": line.strip()[:100] # 截取部分上下文
                    }
                    self.results.append(result)
                    self.matches_found += 1
                    logger.warning(f"Found {card_type}: {path_display} (Line {line_idx})")

    def scan_archive(self, file_path, current_depth, archive_chain):
        """处理压缩包 (递归)"""
        if current_depth > self.max_archive_depth:
            return

        temp_dir = tempfile.mkdtemp()
        new_chain = archive_chain + [os.path.basename(file_path)]
        
        try:
            # 识别并解压
            if zipfile.is_zipfile(file_path):
                with zipfile.ZipFile(file_path, 'r') as z:
                    z.extractall(temp_dir)
            elif tarfile.is_tarfile(file_path):
                with tarfile.open(file_path, 'r') as t:
                    t.extractall(temp_dir)
            elif file_path.endswith('.gz'):
                # Gzip 通常是单文件，解压后去除 .gz 后缀
                out_name = os.path.join(temp_dir, os.path.basename(file_path)[:-3])
                with gzip.open(file_path, 'rb') as f_in:
                    with open(out_name, 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
            else:
                return # 不是支持的压缩包

            # 递归扫描解压后的目录
            self.scan_directory(temp_dir, current_depth + 1, new_chain)

        except Exception as e:
            logger.error(f"Error extracting {file_path}: {e}")
        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)

    def process_single_file(self, file_path, current_depth=0, archive_chain=None):
        """处理单个文件入口"""
        if self.abort_signal: return

        if archive_chain is None: archive_chain = []
        
        ext = os.path.splitext(file_path)[1].lower()
        if ext in self.exclude_exts:
            return

        # 检查是否为压缩包
        if ext in ['.zip', '.tar', '.gz', '.tgz'] or zipfile.is_zipfile(file_path):
            self.scan_archive(file_path, current_depth, archive_chain)
            return

        # 扫描内容
        content = self.extract_text(file_path)
        self.process_content(content, file_path, archive_chain)

    def scan_directory(self, path, depth=0, chain=None):
        """扫描目录"""
        files_to_scan = []
        for root, dirs, files in os.walk(path):
            for file in files:
                files_to_scan.append(os.path.join(root, file))

        # 使用线程池并发处理文件
        # 注意：如果是在压缩包解压后的临时目录中，不建议开启过多线程以免IO冲突严重
        # 这里为了简化，主流程开启线程池，递归内部串行或由主池调度
        
        if depth == 0 and self.threads > 1:
            with ThreadPoolExecutor(max_workers=self.threads) as executor:
                futures = [executor.submit(self.process_single_file, f, depth, chain) for f in files_to_scan]
                for _ in as_completed(futures):
                    self.total_files += 1
                    if self.total_files % 100 == 0:
                        sys.stdout.write(f"\rScanned {self.total_files} files...")
                        sys.stdout.flush()
        else:
            # 递归深层或临时目录直接串行处理
            for f in files_to_scan:
                self.process_single_file(f, depth, chain)
                if depth == 0: # 只有顶层计数
                    self.total_files += 1

    def run(self):
        logger.info(f"Starting scan on: {self.root_path}")
        try:
            if os.path.isfile(self.root_path):
                self.process_single_file(self.root_path)
            else:
                self.scan_directory(self.root_path)
        except KeyboardInterrupt:
            logger.info("\nScan interrupted by user.")
            self.abort_signal = True
        
        sys.stdout.write("\n")
        logger.info(f"Scan complete. Processed {self.total_files} files. Found {self.matches_found} matches.")
        return self.results

def main():
    parser = argparse.ArgumentParser(description="Advanced Credit Card Scanner")
    parser.add_argument("path", help="Path to scan")
    parser.add_argument("--json", help="Output results to JSON file", action="store_true")
    parser.add_argument("--mask", help="Mask credit card numbers in output", action="store_true")
    parser.add_argument("-t", "--threads", type=int, default=4, help="Number of threads (default: 4)")
    parser.add_argument("-e", "--exclude", help="Comma separated extensions to exclude (e.g. .exe,.dll)", default=".exe,.dll,.so,.dylib")
    parser.add_argument("--ignore-list", help="File containing numbers to ignore")
    
    args = parser.parse_args()

    # 读取忽略列表
    ignore_set = set()
    if args.ignore_list and os.path.exists(args.ignore_list):
        with open(args.ignore_list, 'r') as f:
            ignore_set = set(f.read().splitlines())

    scanner = CreditCardScanner(
        root_path=args.path,
        ignore_list=ignore_set,
        exclude_exts=args.exclude.split(','),
        mask=args.mask,
        threads=args.threads
    )

    results = scanner.run()

    if args.json:
        out_file = f"scan_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(out_file, 'w') as f:
            json.dump(results, f, indent=4)
        logger.info(f"Results saved to {out_file}")

if __name__ == "__main__":
    main()
