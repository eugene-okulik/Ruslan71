def process_line(line):
    number = int(line.split(':')[-1].strip())
    print(number + 10)

lines = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]

for line in lines:
    process_line(line)
