import random

salary = int(input("Введите вашу зарплату: "))

bonus = random.choice([True, False])

if bonus:
    total = salary + random.randint(1, 5000)
else:
    total = salary

print(f"{salary}, {bonus} - '${total}'")

