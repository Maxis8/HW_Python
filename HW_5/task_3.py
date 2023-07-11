# 3. Создайте функцию генератор чисел Фибоначчи (см. Википедию)

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


print(fib())
d = iter(fib())
print(next(d))
print(next(d))

