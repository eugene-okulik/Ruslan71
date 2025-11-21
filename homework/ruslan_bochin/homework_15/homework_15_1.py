import mysql.connector

# Подключение к базе
db = mysql.connector.connect(
    host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
    user="st-onl",
    passwd="AVNS_tegPDkI5BlB2lW5eASC",
    database="st-onl",
    port=25060
)

cursor = db.cursor(dictionary=True)

cursor.execute(
    "INSERT INTO students (name, second_name) VALUES (%s, %s)",
    ("Иван", "Иванов")
)
student_id = cursor.lastrowid
print(f"Создан студент: id={student_id}")

cursor.execute(
    "INSERT INTO `groups` (title) VALUES (%s)",
    ("Группа А",)
)
group_id = cursor.lastrowid
print(f"Создана группа: id={group_id}")

cursor.execute(
    "UPDATE students SET group_id = %s WHERE id = %s",
    (group_id, student_id)
)
print(f"Студент {student_id} добавлен в группу {group_id}")

books = ["Математика 101", "Физика для начинающих", "История мира"]
book_ids = []
for title in books:
    cursor.execute(
        "INSERT INTO books (title) VALUES (%s)",
        (title,)
    )
    book_ids.append(cursor.lastrowid)
print(f"Созданы книги: {book_ids}")

subjects = ["Математика", "Физика", "История"]
subject_ids = []
for title in subjects:
    cursor.execute(
        "INSERT INTO subjects (title) VALUES (%s)",
        (title,)
    )
    subject_ids.append(cursor.lastrowid)
print(f"Созданы предметы: {subject_ids}")

lessons_per_subject = {
    "Математика": ["Алгебра", "Геометрия"],
    "Физика": ["Механика", "Оптика"],
    "История": ["Древний мир", "Новейшая история"]
}

lesson_ids = []
for subj_name, lesson_list in lessons_per_subject.items():
    subj_index = subjects.index(subj_name)
    subj_id = subject_ids[subj_index]
    for lesson_name in lesson_list:
        cursor.execute(
            "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)",
            (lesson_name, subj_id)
        )
        lesson_ids.append(cursor.lastrowid)
print(f"Созданы уроки: {lesson_ids}")

marks = ["5", "4", "5", "4", "5", "4"]
for lesson_id, mark in zip(lesson_ids, marks):
    cursor.execute(
        "INSERT INTO marks (student_id, lesson_id, value) VALUES (%s, %s, %s)",
        (student_id, lesson_id, mark)
    )
print(f"Добавлены оценки студенту {student_id}")

db.commit()

cursor.execute("""
    SELECT m.value AS mark, l.title AS lesson_name, s.title AS subject_name
    FROM marks m
    JOIN lessons l ON m.lesson_id = l.id
    JOIN subjects s ON l.subject_id = s.id
    WHERE m.student_id = %s
""", (student_id,))
print("\nОценки студента:")
for row in cursor.fetchall():
    print(row)

cursor.execute("""
    SELECT st.name AS student_name, st.second_name, g.title AS group_title,
           m.value AS mark, l.title AS lesson_name, s.title AS subject_name
    FROM students st
    LEFT JOIN `groups` g ON st.group_id = g.id
    LEFT JOIN marks m ON st.id = m.student_id
    LEFT JOIN lessons l ON m.lesson_id = l.id
    LEFT JOIN subjects s ON l.subject_id = s.id
    WHERE st.id = %s
""", (student_id,))
print("\nПолная информация о студенте:")
for row in cursor.fetchall():
    print(row)

db.close()
