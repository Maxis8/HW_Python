# 2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num1 = int(input('Enter number: '))
rank = int(16)


def ranks(num: int, r) -> str:
    result = ''
    while num >= 1:
        res = num % r

        if res == 10:
            res = 'a'
        if res == 11:
            res = 'b'
        if res == 12:
            res = 'c'
        if res == 13:
            res = 'd'
        if res == 14:
            res = 'e'
        if res == 15:
            res = 'f'
        result += str(res)
        num = num // r
    return result[::-1]


print(ranks(num1, rank))
b = hex(num1)
print(b)

