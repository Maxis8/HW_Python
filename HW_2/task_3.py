# 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.
import fractions


def multi_fraction(n1, n2):
    b1 = list(map(int, n1.split('/')))
    b2 = list(map(int, n2.split('/')))
    a = b1[0] * b2[0]
    b = b1[1] * b2[1]
    for i in range(a, 1, -1):
        if a % i == 0 and b % i == 0:
            a = int(a / i)
            b = int(b / i)

    res = f'{a}/{b}'
    return res


def sum_fraction(k1, k2):
    b1 = list(map(int, k1.split('/')))
    b2 = list(map(int, k2.split('/')))
    c1 = b1[1]
    c2 = b2[1]
    while c2 % c1 != 0:
        c2 += b2[1]
    c = int(b1[0] * (c2 / b1[1]) + (b2[0] * (c2 / b2[1])))
    for i in range(c, 1, -1):
        if c % i == 0 and c2 % i == 0:
            c = int(c / i)
            c2 = int(c2 / i)

    res = f'{c}/{c2}'
    return res


a1 = '187/57'
a2 = '169/1479'
print(multi_fraction(a1, a2))
print(sum_fraction(a1, a2))
a1 = fractions.Fraction(187, 57)
a2 = fractions.Fraction(169, 1479)
print(f'{a1 * a2} ')
print(f'{a1 + a2} ')

