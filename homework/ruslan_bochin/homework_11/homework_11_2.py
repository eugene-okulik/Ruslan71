class Book:
    material = "бумага"
    has_text = True

    def __init__(self, title, author, pages, isbn, reserved=False):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved

    def __str__(self):
        base = f"Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, материал: {self.material}"
        if self.reserved:
            return base + ", зарезервирована"
        return base


class Textbook(Book):
    def __init__(self, title, author, pages, isbn, subject, grade, has_tasks, reserved=False):
        super().__init__(title, author, pages, isbn, reserved)
        self.subject = subject
        self.grade = grade
        self.has_tasks = has_tasks

    def __str__(self):
        base = (
            f"Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, "
            f"предмет: {self.subject}, класс: {self.grade}"
        )
        if self.reserved:
            return base + ", зарезервирована"
        return base


t1 = Textbook("Алгебра", "Иванов", 200, "111-222", "Математика", 9, True)
t2 = Textbook("История России", "Петров", 250, "333-444", "История", 7, False)
t3 = Textbook("География материков", "Сидоров", 180, "555-666", "География", 6, True)
t4 = Textbook("Физика", "Кузнецов", 300, "777-888", "Физика", 8, True)

t2.reserved = True

textbooks = [t1, t2, t3, t4]

for tb in textbooks:
    print(tb)
