import sys

sys.set_int_max_str_digits(1_000_000_000)

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


gen = fibonacci()
targets = [5, 200, 1000, 100_000]
results = {}

for i, num in enumerate(gen, start=1):
    if i in targets:
        results[i] = num
        if len(results) == len(targets):
            break

for k in targets:
    num = results[k]
    print(f"{k}-е число Фибоначчи содержит {len(str(num))} цифр.")
