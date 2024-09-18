# by huowuzhao
import os
import sys
import signal
import subprocess
import tempfile
import shutil
import json
from datetime import datetime
import textract
import re

# 全局变量定义
logfilename = None
logfilefd = None
total_files_processed = 0
total_cards_found = 0
extracted_archive_count = 0
skipped_executable_count = 0
ignore_list = set()
file_extensions_to_exclude = set()
results = []  # 用于存储结果的全局列表
json_output_enabled = False  # JSON 输出的开关
mask_card_numbers = False  # 脱敏功能的开关
extracted_file_path_stack = []  # 用于记录解压文件的路径栈

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
    PDF = 'PDF'
    MS_OFFICE = 'MS_OFFICE'
    BINARY = 'BINARY'

# 信用卡检测逻辑和算法
def luhn_check(card_number):
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
    card_pattern = r'\b(?:\d[ -]*?){13,16}\b'
    matches = re.finditer(card_pattern, text)

    potential_cards = []

    for match in matches:
        card_number = match.group()
        cleaned_number = re.sub(r'[^0-9]', '', card_number)
        if 13 <= len(cleaned_number) <= 16 and luhn_check(cleaned_number):
            start_offset = match.start()
            potential_cards.append((card_number, line_number, start_offset))

    return potential_cards

# 信用卡类型检测函数
def get_card_type(card_number):
    cleaned_number = re.sub(r'[^0-9]', '', card_number)
    if is_visa(cleaned_number):
        return 'VISA'
    elif is_mastercard(cleaned_number):
        return 'MasterCard'
    elif is_amex(cleaned_number):
        return 'American Express'
    elif is_discover(cleaned_number):
        return 'Discover'
    elif is_jcb(cleaned_number):
        return 'JCB'
    elif is_diners_club(cleaned_number):
        return 'Diners Club'
    else:
        return 'Unknown'

def is_visa(card_number):
    return len(card_number) in [13, 16] and card_number[0] == '4'

def is_mastercard(card_number):
    return len(card_number) == 16 and 51 <= int(card_number[:2]) <= 55

def is_amex(card_number):
    return len(card_number) == 15 and card_number[:2] in ['34', '37']

def is_discover(card_number):
    return len(card_number) == 16 and card_number[:4] == '6011'

def is_jcb(card_number):
    return len(card_number) in [15, 16] and (3528 <= int(card_number[:4]) <= 3589)

def is_diners_club(card_number):
    return len(card_number) == 14 and (300 <= int(card_number[:3]) <= 305 or card_number[:2] in ['36', '38'])

def mask_card_number(card_number):
    cleaned_number = re.sub(r'[^0-9]', '', card_number)
    if len(cleaned_number) <= 4:
        return card_number
    return card_number[:4] + "#" * (len(cleaned_number) - 8) + cleaned_number[-4:]

# 初始化模块
def initialise_mods():
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
        result = subprocess.run(['file', '--mime-type', '-b', filename], stdout=subprocess.PIPE, text=True)
        output = result.stdout.lower()

        if 'text/plain' in output:
            return FileType.ASCII
        elif 'executable' in output or 'sharedlib' in output or 'octet-stream' in output:
            return FileType.BINARY
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
        elif 'application/gzip' in output:
            return FileType.GZIP
        elif 'application/pdf' in output:
            return FileType.PDF
        elif 'msword' in output or 'mspowerpoint' in output or 'ms-excel' in output or 'officedocument' in output:
            return FileType.MS_OFFICE
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
    global total_files_processed
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if is_excluded_file(file_path):
                continue
            process_file(file_path)

# 检查文件类型是否排除
def is_excluded_file(filename):
    ext = os.path.splitext(filename)[1].lower()
    return ext in file_extensions_to_exclude

# 文件扫描
def process_file(filename):
    global total_files_processed
    total_files_processed += 1
    filetype = detect_file_type(filename)

    if filetype in (FileType.BINARY, FileType.EXECUTABLE, FileType.IMAGE, FileType.VIDEO, FileType.AUDIO):
        print(f"Skipping unsupported file type: {filename}")
        return

    # 将当前文件路径加入路径栈
    extracted_file_path_stack.append(filename)

    if filetype == FileType.ZIP:
        unzip_and_parse(filename)
    elif filetype == FileType.GZIP:
        gunzip_and_parse(filename)
    elif filetype == FileType.TAR:
        untar_and_parse(filename)
    elif filetype in (FileType.PDF, FileType.MS_OFFICE):
        parse_with_textract(filename)
    else:
        search_file_content(filename)

    # 处理完成后，从路径栈中移除当前文件
    extracted_file_path_stack.pop()

# 使用textract解析文件
def parse_with_textract(filename):
    global total_cards_found
    try:
        text = textract.process(filename).decode('utf-8', errors='ignore')
        lines = text.splitlines()
        detected_cards = []

        for i, line in enumerate(lines, start=1):
            detected_cards.extend(find_potential_credit_card_numbers(line, line_number=i))

        for card, line_number, start_offset in detected_cards:
            card_type = get_card_type(card)
            if card not in ignore_list and card_type != 'Unknown':
                output_path = " -> ".join(extracted_file_path_stack)

                displayed_card = mask_card_number(card) if mask_card_numbers else card

                context = get_card_context(lines, line_number, card) if mask_card_numbers else get_card_context(lines, line_number)

                print(f"Detected {card_type} card in {output_path} at line {line_number}: {displayed_card}")
                print(f"Context:\n{context}")

                results.append({
                    "filename": output_path,
                    "line_number": line_number,
                    "card_number": displayed_card,
                    "card_type": card_type,
                    "context": context
                })
                total_cards_found += 1
    except Exception as e:
        print(f"Error processing file {filename} with textract: {e}")

# 获取信用卡号的上下文
def get_card_context(lines, line_number, card_number=None):
    start_line = max(line_number - 3, 0)
    end_line = min(line_number + 2, len(lines))

    context = "\n".join(lines[start_line:end_line])

    if card_number and mask_card_numbers:
        masked_card = mask_card_number(card_number)
        context = context.replace(card_number, masked_card)

    return context

# 文件内容扫描
def search_file_content(filename):
    global total_cards_found
    try:
        with open(filename, 'r', errors='ignore') as f:
            lines = f.readlines()
            detected_cards = []
            for line_number, line in enumerate(lines, start=1):
                detected_cards.extend(find_potential_credit_card_numbers(line, line_number=line_number))

            for card, line_number, start_offset in detected_cards:
                card_type = get_card_type(card)
                if card not in ignore_list and card_type != 'Unknown':
                    output_path = " -> ".join(extracted_file_path_stack)

                    displayed_card = mask_card_number(card) if mask_card_numbers else card

                    context = get_card_context(lines, line_number, card) if mask_card_numbers else get_card_context(lines, line_number)

                    print(f"Detected {card_type} card in {output_path} at line {line_number}: {displayed_card}")
                    print(f"Context:\n{context}")

                    results.append({
                        "filename": output_path,
                        "line_number": line_number,
                        "card_number": displayed_card,
                        "card_type": card_type,
                        "context": context
                    })
                    total_cards_found += 1
    except Exception as e:
        print(f"Error reading file {filename}: {e}")

# 解压ZIP文件
def unzip_and_parse(filename):
    global extracted_archive_count
    temp_dir = tempfile.mkdtemp()
    try:
        extracted_archive_count += 1
        subprocess.run(['unzip', '-o', '-d', temp_dir, filename], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                process_file(file_path)
    finally:
        shutil.rmtree(temp_dir)

# 解压GZIP文件
def gunzip_and_parse(filename):
    global extracted_archive_count
    temp_file = tempfile.mkstemp()[1]
    try:
        extracted_archive_count += 1
        with open(temp_file, 'wb') as f_out:
            subprocess.run(['gzip', '-d', '-c', filename], stdout=f_out)

        process_file(temp_file)
    finally:
        os.remove(temp_file)

# 解压TAR文件
def untar_and_parse(filename):
    global extracted_archive_count
    temp_dir = tempfile.mkdtemp()
    try:
        extracted_archive_count += 1
        subprocess.run(['tar', '-xf', filename, '-C', temp_dir], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                process_file(file_path)
    finally:
        shutil.rmtree(temp_dir)

# 清理和退出
def cleanup():
    global results
    print(f"\nTotal files processed: {total_files_processed}")
    print(f"Total credit card matches: {total_cards_found}")
    print(f"Archives extracted: {extracted_archive_count}")
    print(f"Skipped executables: {skipped_executable_count}")

    if json_output_enabled:
        with open('result_json.json', 'w') as json_file:
            json.dump(results, json_file, indent=4)
        print("\nResults have been written to result_json.json.")

# 主函数
def main():
    global ignore_list, file_extensions_to_exclude, json_output_enabled, mask_card_numbers

    if len(sys.argv) < 2:
        print("Usage: python ccsrch.py <options> <start_path>")
        sys.exit(1)

    start_path = sys.argv[-1]
    initialise_mods()
    setup_signal_handlers()

    for i, arg in enumerate(sys.argv):
        if arg == '--json-output':
            json_output_enabled = True
        elif arg == '--mask':
            mask_card_numbers = True
        elif arg == '-i' and i + 1 < len(sys.argv):
            ignore_list = read_ignore_list(sys.argv[i + 1])
        elif arg == '-n' and i + 1 < len(sys.argv):
            file_extensions_to_exclude = set(sys.argv[i + 1].split(','))

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
