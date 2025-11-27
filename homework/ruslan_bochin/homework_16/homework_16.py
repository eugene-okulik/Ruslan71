import csv
import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSW = os.getenv("DB_PASSW")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = int(os.getenv("DB_PORT") or 3306)

conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    passwd=DB_PASSW,
    database=DB_NAME,
    port=DB_PORT,
    use_pure=True
)

cursor = conn.cursor(dictionary=True, buffered=True)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(BASE_DIR, "hw_data", "data.csv")

if not os.path.exists(csv_file):
    raise FileNotFoundError(f"CSV файл не найден: {csv_file}")

with open(csv_file, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    csv_rows = list(reader)

missing_rows = []

for row in csv_rows:
    cursor.execute("""
        SELECT st.id
        FROM students st
        JOIN `groups` g ON st.group_id = g.id
        WHERE st.name=%s AND st.second_name=%s AND g.title=%s
    """, (row["name"], row["second_name"], row["group_title"]))
    student = cursor.fetchone()
    if not student:
        missing_rows.append(row)
        continue

    student_id = student["id"]

    cursor.execute("""
        SELECT l.id
        FROM lessons l
        JOIN subjects s ON l.subject_id = s.id
        WHERE l.title=%s AND s.title=%s
    """, (row["lesson_title"], row["subject_title"]))
    lesson = cursor.fetchone()
    if not lesson:
        missing_rows.append(row)
        continue

    lesson_id = lesson["id"]

    cursor.execute("""
        SELECT m.id
        FROM marks m
        WHERE m.student_id=%s AND m.lesson_id=%s AND m.value=%s
    """, (student_id, lesson_id, row["mark_value"]))
    mark = cursor.fetchone()
    if not mark:
        missing_rows.append(row)

if missing_rows:
    print("В базе нет следующих данных из CSV:")
    for r in missing_rows:
        print(r)
else:
    print("Все данные из CSV есть в базе.")

cursor.close()
conn.close()
