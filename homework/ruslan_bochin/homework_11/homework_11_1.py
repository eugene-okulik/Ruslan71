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


book1 = Book("Идиот", "Ф. Достоевский", 500, "978-5-389-07462-8")
book2 = Book("Мастер и Маргарита", "М. Булгаков", 420, "978-5-17-118366-4")
book3 = Book("1984", "Джордж Оруэлл", 350, "978-5-389-07471-0")
book4 = Book("Преступление и наказание", "Ф. Достоевский", 670, "978-5-389-06224-3")
book5 = Book("Три товарища", "Эрих Мария Ремарк", 480, "978-5-389-07339-3")

book3.reserved = True

books = [book1, book2, book3, book4, book5]

for b in books:
    print(b)
