import argparse
import os
from datetime import datetime


def parse_args():
    parser = argparse.ArgumentParser(description="Log Analyzer")
    parser.add_argument("path", help="Путь к файлу или директории с логами")
    parser.add_argument("--text", required=True, help="Текст, который нужно найти")
    return parser.parse_args()


def get_files(path):
    if os.path.isfile(path):
        return [path]

    if os.path.isdir(path):
        return [
            os.path.join(path, f)
            for f in os.listdir(path)
            if os.path.isfile(os.path.join(path, f))
        ]

    raise FileNotFoundError(f"Путь '{path}' не найден")


def read_log_blocks(filepath):
    blocks = {}
    current_time = None
    current_lines = []

    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            stripped = line.strip()

            try:
                timestamp = datetime.strptime(stripped[:19], "%Y-%m-%d %H:%M:%S")

                if current_time is not None:
                    blocks[current_time] = current_lines

                current_time = timestamp
                current_lines = [line]

            except ValueError:
                if current_time is not None:
                    current_lines.append(line)

        if current_time is not None:
            blocks[current_time] = current_lines

    return blocks


def extract_snippet(line, target):
    words = line.split()
    for i, word in enumerate(words):
        if target in word:
            start = max(0, i - 5)
            end = i + 6
            return " ".join(words[start:end])
    return None


def search_in_blocks(filepath, blocks, target):
    results = []

    for timestamp, lines in blocks.items():
        for lineno, line in enumerate(lines, start=1):
            if target in line:
                snippet = extract_snippet(line, target)
                results.append({
                    "file": filepath,
                    "time": timestamp,
                    "line": lineno,
                    "snippet": snippet
                })

    return results


def main():
    args = parse_args()
    files = get_files(args.path)
    target = args.text

    total = 0

    for file in files:
        blocks = read_log_blocks(file)
        matches = search_in_blocks(file, blocks, target)

        for result in matches:
            total += 1
            print("=" * 90)
            print(f"Файл: {result['file']}")
            print(f"Время ошибки: {result['time']}")
            print(f"Строка в блоке: {result['line']}")
            print(f"Фрагмент: {result['snippet']}")

    if total == 0:
        print("Совпадений не найдено.")
    else:
        print("=" * 90)
        print(f"Всего найденных совпадений: {total}")


if __name__ == "__main__":
    main()
