#by huowuzhao
import os
import sys
import signal
import subprocess
import tempfile
import shutil
import json  # 引入json模块用于JSON格式输出
from datetime import datetime
import textract  # 引入textract包用于处理各种文档类型

# 全局变量定义
logfilename = None
logfilefd = None
total_count = 0
extracted_archive_count = 0
skipped_executable_count = 0
currfilename = None
skipchars = [' ', '\n', '\r', '-']
skipchar_count = len(skipchars)
ignore_list = set()
file_extensions_to_exclude = set()
processing_docx = False
processing_xlsx = False
results = []  # 用于存储结果的全局列表
json_output_enabled = False  # JSON 输出的开关
current_parent_path = ""  # 保存压缩文件的路径

# 文件类型枚举
class FileType:
    UNKNOWN = 'UNKNOWN'
    ASCII = 'ASCII'
    EXECUTABLE = 'EXECUTABLE'
    IMAGE = 'IMAGE'
    VIDEO = 'VIDEO'
    AUDIO = 'AUDIO'
    TAR = 'TAR'
    ZIP = 'ZIP'
    GZIP = 'GZIP'
    XML = 'XML'
    PDF = 'PDF'
    OTT = 'OTT'
    ODT = 'ODT'
    OTS = 'OTS'
    ODS = 'ODS'
    MS_EXCEL = 'MS_EXCEL'
    MS_WORD = 'MS_WORD'
    MS_WORDX = 'MS_WORDX'
    MS_EXCELX = 'MS_EXCELX'
    BINARY = 'BINARY'

# 信用卡检测逻辑和算法

def luhn_check(card_number):
    # 使用Luhn算法验证信用卡号
    digits = [int(ch) for ch in str(card_number)]
    checksum = 0
    reverse_digits = digits[::-1]

    for i, digit in enumerate(reverse_digits):
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit

    return checksum % 10 == 0

def find_potential_credit_card_numbers(text, line_number=None):
    # 去除非数字字符，保持原始位置索引
    cleaned_text = ""
    original_indices = []

    for i, char in enumerate(text):
        if char.isdigit():
            cleaned_text += char
            original_indices.append(i)

    potential_cards = []

    # 从清理过的文本中检测潜在的信用卡号
    current_number = ""
    current_indices = []

    for i, char in enumerate(cleaned_text):
        current_number += char
        current_indices.append(original_indices[i])

        # 检查长度和Luhn算法
        if 13 <= len(current_number) <= 16 and luhn_check(current_number):
            potential_cards.append((current_number, line_number, current_indices))
            current_number = ""
            current_indices = []

    # 最后一个可能的卡号检查
    if 13 <= len(current_number) <= 16 and luhn_check(current_number):
        potential_cards.append((current_number, line_number, current_indices))

    return potential_cards

# 信用卡类型检测函数
def get_card_type(card_number):
    """检测信用卡类型"""
    if is_visa(card_number):
        return 'VISA'
    elif is_mastercard(card_number):
        return 'MasterCard'
    elif is_amex(card_number):
        return 'American Express'
    elif is_discover(card_number):
        return 'Discover'
    elif is_jcb(card_number):
        return 'JCB'
    elif is_diners_club(card_number):
        return 'Diners Club'
    else:
        return 'Unknown'

def is_visa(card_number):
    """检测Visa卡"""
    return len(card_number) in [13, 16] and card_number[0] == '4'

def is_mastercard(card_number):
    """检测MasterCard卡"""
    return len(card_number) == 16 and 51 <= int(card_number[:2]) <= 55

def is_amex(card_number):
    """检测American Express卡"""
    return len(card_number) == 15 and card_number[:2] in ['34', '37']

def is_discover(card_number):
    """检测Discover卡"""
    return len(card_number) == 16 and card_number[:4] == '6011'

def is_jcb(card_number):
    """检测JCB卡"""
    return len(card_number) in [15, 16] and (
        3528 <= int(card_number[:4]) <= 3589)

def is_diners_club(card_number):
    """检测Diners Club卡"""
    return len(card_number) == 14 and (300 <= int(card_number[:3]) <= 305 or
                                       card_number[:2] in ['36', '38'])

# 初始化模块
def initialise_mods():
    global skipchars
    global skipchar_count
    skipchars = [' ', '\n', '\r', '-']
    skipchar_count = len(skipchars)
    return True

# 信号处理
def signal_handler(signum, frame):
    cleanup()
    sys.exit(0)

def setup_signal_handlers():
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

# 文件类型检测
def detect_file_type(filename):
    try:
        result = subprocess.run(['file', '--mime', '-b', filename], stdout=subprocess.PIPE, text=True)
        output = result.stdout.lower()

        if 'text/plain' in output:
            return FileType.ASCII
        elif 'executable' in output or 'x-sharedlib' in output:
            return FileType.EXECUTABLE
        elif 'image' in output:
            return FileType.IMAGE
        elif 'video' in output:
            return FileType.VIDEO
        elif 'audio' in output:
            return FileType.AUDIO
        elif 'application/x-tar' in output:
            return FileType.TAR
        elif 'application/zip' in output:
            return FileType.ZIP
        elif 'application/x-gzip' in output:
            return FileType.GZIP
        elif 'application/xml' in output:
            return FileType.XML
        elif 'application/pdf' in output:
            return FileType.PDF
        elif 'opendocument.text-template' in output:
            return FileType.OTT
        elif 'opendocument.text' in output:
            return FileType.ODT
        elif 'opendocument.spreadsheet.template' in output:
            return FileType.OTS
        elif 'opendocument.spreadsheet' in output:
            return FileType.ODS
        elif 'application/vnd.ms-excel' in output:
            return FileType.MS_EXCEL
        elif 'application/msword' in output or 'application/vnd.ms-word' in output:
            return FileType.MS_WORD
        else:
            return FileType.UNKNOWN
    except Exception as e:
        print(f"Error detecting file type: {e}")
        return FileType.UNKNOWN

# 忽略列表读取
def read_ignore_list(filename):
    try:
        with open(filename, 'r') as f:
            ignore_numbers = f.read().splitlines()
            return set(ignore_numbers)
    except Exception as e:
        print(f"Error reading ignore list: {e}")
        return set()

# 目录扫描
def process_directory(path):
    global total_count
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if is_allowed_file_type(file_path):
                continue
            total_count += process_file(file_path)

# 文件扫描
def process_file(filename):
    global logfilefd, current_parent_path
    filetype = detect_file_type(filename)

    if filetype in (FileType.EXECUTABLE, FileType.IMAGE, FileType.VIDEO, FileType.AUDIO):
        print(f"Skipping unsupported file type: {filename}")
        return 0

    if filetype == FileType.ZIP:
        return unzip_and_parse(filename)
    elif filetype == FileType.GZIP:
        return gunzip_and_parse(filename)
    elif filetype == FileType.TAR:
        return untar_and_parse(filename)
    elif filetype in (FileType.PDF, FileType.MS_WORD, FileType.MS_WORDX, FileType.MS_EXCEL, FileType.MS_EXCELX):
        return parse_with_textract(filename)
    else:
        return search_file_content(filename)

# 使用textract解析文件
def parse_with_textract(filename):
    global total_count, results, current_parent_path
    try:
        text = textract.process(filename).decode('utf-8')
        lines = text.splitlines()
        detected_cards = []

        for i, line in enumerate(lines, start=1):
            detected_cards.extend(find_potential_credit_card_numbers(line, line_number=i))

        for card, line_number, original_indices in detected_cards:
            card_type = get_card_type(card)
            if card not in ignore_list and card_type != 'Unknown':  # 跳过Unknown卡
                # 使用组合路径
                output_path = os.path.join(current_parent_path, os.path.basename(filename)) if current_parent_path else filename
                print(f"Detected {card_type} card in {output_path} at line {line_number}: {card}")
                results.append({
                    "filename": output_path,
                    "line_number": line_number,
                    "card_number": card,
                    "card_type": card_type,
                    "original_indices": original_indices
                })
                total_count += 1
        return len(detected_cards)
    except Exception as e:
        print(f"Error processing file {filename} with textract: {e}")
        return 0

# 检查文件类型是否允许
def is_allowed_file_type(name):
    ext = os.path.splitext(name)[1].lower()
    return ext in file_extensions_to_exclude

# 文件内容扫描
def search_file_content(filename):
    global ignore_list, total_count, results, current_parent_path
    try:
        with open(filename, 'r', errors='ignore') as f:
            detected_cards = []
            for line_number, line in enumerate(f, start=1):
                detected_cards.extend(find_potential_credit_card_numbers(line, line_number=line_number))

            for card, line_number, original_indices in detected_cards:
                card_type = get_card_type(card)
                if card not in ignore_list and card_type != 'Unknown':  # 跳过Unknown卡
                    # 使用组合路径
                    output_path = os.path.join(current_parent_path, os.path.basename(filename)) if current_parent_path else filename
                    print(f"Detected {card_type} card in {output_path} at line {line_number}: {card}")
                    results.append({
                        "filename": output_path,
                        "line_number": line_number,
                        "card_number": card,
                        "card_type": card_type,
                        "original_indices": original_indices
                    })
                    total_count += 1
        return len(detected_cards)
    except Exception as e:
        print(f"Error reading file {filename}: {e}")
        return 0

# 解压ZIP文件
def unzip_and_parse(filename):
    global current_parent_path
    temp_dir = tempfile.mkdtemp()
    try:
        # 保存当前压缩文件的路径
        original_parent_path = current_parent_path
        current_parent_path = filename  # 更新当前父路径

        subprocess.run(['unzip', '-o', '-d', temp_dir, filename], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        process_directory(temp_dir)
    finally:
        shutil.rmtree(temp_dir)
        current_parent_path = original_parent_path  # 恢复父路径
    return 0

# 解压GZIP文件
def gunzip_and_parse(filename):
    global current_parent_path
    temp_file = tempfile.mkstemp()[1]
    try:
        # 保存当前压缩文件的路径
        original_parent_path = current_parent_path
        current_parent_path = filename  # 更新当前父路径

        with open(temp_file, 'wb') as f_out:
            subprocess.run(['gzip', '-d', '-c', filename], stdout=f_out)
        return search_file_content(temp_file)
    finally:
        os.remove(temp_file)
        current_parent_path = original_parent_path  # 恢复父路径

# 解压TAR文件
def untar_and_parse(filename):
    global current_parent_path
    temp_dir = tempfile.mkdtemp()
    try:
        # 保存当前压缩文件的路径
        original_parent_path = current_parent_path
        current_parent_path = filename  # 更新当前父路径

        subprocess.run(['tar', '-xvf', filename, '-C', temp_dir], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        process_directory(temp_dir)
    finally:
        shutil.rmtree(temp_dir)
        current_parent_path = original_parent_path  # 恢复父路径
    return 0

# 清理和退出
def cleanup():
    global results
    if logfilefd:
        logfilefd.close()
    print(f"\nTotal files processed: {total_count}")
    print(f"Total credit card matches: {total_count}")
    print(f"Archives extracted: {extracted_archive_count}")
    print(f"Skipped executables: {skipped_executable_count}")

    # 如果启用JSON输出，将结果写入文件
    if json_output_enabled:
        with open('result_json.json', 'w') as json_file:
            json.dump(results, json_file, indent=4)
        print("\nResults have been written to result_json.json.")

# 主函数
def main():
    global logfilename, logfilefd, ignore_list, file_extensions_to_exclude, json_output_enabled

    if len(sys.argv) < 2:
        print("Usage: python ccsrch.py <options> <start_path>")
        sys.exit(1)

    # 解析命令行参数
    start_path = sys.argv[-1]
    initialise_mods()
    setup_signal_handlers()

    # 读取忽略列表（如果提供）
    for i, arg in enumerate(sys.argv):
        if arg == '--json-output':
            json_output_enabled = True
        elif arg == '-i' and i + 1 < len(sys.argv):
            ignore_list = read_ignore_list(sys.argv[i + 1])
        elif arg == '-n' and i + 1 < len(sys.argv):
            file_extensions_to_exclude = set(sys.argv[i + 1].split(','))

    # 扫描目录或文件
    if os.path.isdir(start_path):
        process_directory(start_path)
    elif os.path.isfile(start_path):
        process_file(start_path)
    else:
        print("Invalid path specified.")
        sys.exit(1)

    cleanup()

if __name__ == "__main__":
    main()
