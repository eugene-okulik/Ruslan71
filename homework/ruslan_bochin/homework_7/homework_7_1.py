secret_number = 7
guess = None

while guess != secret_number:
    guess = int(input("Угадайте цифру от 0 до 9: "))
    if guess != secret_number:
        print("Попробуй снова")
    else:
        print("Поздравляю! Вы угадали!")
