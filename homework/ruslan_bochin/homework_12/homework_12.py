class Flower:
    def __init__(self, color, stem_length, price, lifetime_days):
        self.color = color
        self.stem_length = stem_length
        self.price = price
        self.lifetime_days = lifetime_days  # время жизни в днях

    def __str__(self):
        return (f"{self.__class__.__name__} (цвет: {self.color}, "
                f"длина стебля: {self.stem_length} см, "
                f"цена: {self.price} руб., "
                f"время жизни: {self.lifetime_days} дней)")


class Rose(Flower):
    pass


class Tulip(Flower):
    pass


class Lily(Flower):
    pass


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def price(self):
        return sum(f.price for f in self.flowers)

    def average_lifetime(self):
        return sum(f.lifetime_days for f in self.flowers) / len(self.flowers)

    def sort_by(self, attribute):
        """
        attribute — строка:
        'color', 'stem', 'price', 'lifetime'
        """
        mapping = {
            "color": "color",
            "stem": "stem_length",
            "price": "price",
            "lifetime": "lifetime_days"
        }
        key_attr = mapping.get(attribute)

        if key_attr is None:
            raise ValueError("Неизвестный параметр сортировки")

        self.flowers.sort(key=lambda f: getattr(f, key_attr))

    def find_by_lifetime(self, min_days):
        return [f for f in self.flowers if f.lifetime_days >= min_days]

    def __str__(self):
        text = "Букет:\n"
        for f in self.flowers:
            text += "  - " + str(f) + "\n"
        text += f"Стоимость: {self.price()} руб.\n"
        text += f"Среднее время увядания: {self.average_lifetime():.1f} дней\n"
        return text


r1 = Rose("красный", 40, 150, 7)
r2 = Rose("белый", 45, 180, 8)
t1 = Tulip("желтый", 35, 90, 5)
l1 = Lily("белый", 50, 220, 10)
t2 = Tulip("розовый", 30, 95, 4)

bouquet = Bouquet([r1, r2, t1, l1, t2])

print(bouquet)

bouquet.sort_by("price")
print("\nБукет после сортировки по цене:")
print(bouquet)

found = bouquet.find_by_lifetime(7)
print("\nЦветы с временем жизни ≥ 7 дней:")
for f in found:
    print("  -", f)
