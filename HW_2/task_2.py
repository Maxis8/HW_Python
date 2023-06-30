# 2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num1 = int(input('Enter number: '))
RANK = 16


def ranks(num: int, rank: int) -> str:
    lst = []
    while num > 0:
        num, f = divmod(num, rank)
        lst.append(str(f))

    return ''.join(lst[::-1])


print(ranks(num1, RANK))
b = hex(num1)
print(b)

