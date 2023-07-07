# 4. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

import decimal
import datetime


def refill(acc):
    while True:
        global log
        my_sum = decimal.Decimal(input('Enter sum refill account: '))
        if my_sum < 50 or my_sum % 50 != 0:
            continue
        else:
            log = my_sum
            acc = acc + my_sum
        return acc


def take_off(t):
    LOW_LIMIT = decimal.Decimal(30)
    HI_LIMIT = decimal.Decimal(600)
    global log
    while True:
        my_sum = decimal.Decimal(input('Enter take off sum: '))
        percent = my_sum / 100 * decimal.Decimal(1.5)
        j = t
        if percent < 30:
            t = t - my_sum - LOW_LIMIT
            log = my_sum
            if t < 0:
                t = j
                print('Insufficient funds!!!')

        elif percent > 600:
            t = t - my_sum - HI_LIMIT
            log = my_sum
            if t < 0:
                t = j
                print('Insufficient funds!!!')

        else:
            t = t - my_sum - percent
            log = my_sum
            if t < 0:
                t = j
                print('Insufficient funds!!!')

        return t


def check_money(m, c):
    if m > 5000000:
        m -= m / 10
    if c % 3 == 0:
        m += decimal.Decimal(m / 100) * 3
    return m, c
menu = """
1. Refill account
2. Take off account
3. Exit
"""

log = 0


def menus():
    money = 0
    count = 1
    global log
    history = []
    while True:
        print(menu)
        check_money(money, count)
        print(f'Money = {money}\n')
        choice = int(input('Enter action: '))

        match choice:

            case 1:
                money = refill(money)
                history.append(f' You add: {log}: date: {datetime.datetime.today()} ')
                count += 1
            case 2:
                money = take_off(money)
                history.append(f' You did take: {log}: date: {datetime.datetime.today()}')
                count += 1
            case 3:
                print(money)
                print(*history)
                break


menus()

