def operation_controller(func):
    def wrapper(first, second):
        if first == second:
            op = '+'
        elif first > second:
            op = '-'
        elif second > first:
            op = '/'
        if first < 0 or second < 0:
            op = '*'

        return func(first, second, op)

    return wrapper


@operation_controller
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second
    else:
        raise ValueError("Неизвестная операция")


a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

result = calc(a, b)
print("Результат:", result)
