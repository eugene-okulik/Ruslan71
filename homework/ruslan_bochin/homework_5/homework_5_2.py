one = 'результат операции: 42'
two = 'результат операции: 514'
three = 'результат работы программы: 9'

text = one
colon_index = text.index(":")
number_str = text[colon_index + 2:]
number = int(number_str)
print(number + 10)

text = two
colon_index = text.index(":")
number_str = text[colon_index + 2:]
number = int(number_str)
print(number + 10)

text = three
colon_index = text.index(":")
number_str = text[colon_index + 2:]
number = int(number_str)
print(number + 10)