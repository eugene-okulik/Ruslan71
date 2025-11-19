import os
from datetime import datetime, timedelta

base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

file_path = os.path.join(base_dir, "eugene_okulik", "hw_13", "data.txt")
new_file_path = os.path.join(os.path.dirname(__file__), "data2.txt")

print("Путь к data.txt:", file_path)

actions = {
    "недел": lambda d: d + timedelta(weeks=1),
    "день нед": lambda d: d.strftime("%A"),
    "дней назад": lambda d: (datetime.now() - d).days
}


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line


def extract_date_and_action(line):
    # Структура строки: номер дата - текст
    parts = line.strip().split(" ", 2)
    date_str = parts[1]
    action_text = parts[2].lstrip("-").strip().lower()
    return date_str, action_text


def get_action_key(text):
    return next(k for k in actions if k in text)


def process_line(date_str, action_text):
    date_obj = datetime.fromisoformat(date_str)
    key = get_action_key(action_text)
    return actions[key](date_obj)


with open(new_file_path, "w", encoding="utf-8") as out:
    for line in read_file(file_path):
        if not line.strip():
            continue
        date_str, action_text = extract_date_and_action(line)
        result = process_line(date_str, action_text)
        out.write(f"{line.strip()} → {result}\n")

print("Готово! Результат записан в:", new_file_path)
