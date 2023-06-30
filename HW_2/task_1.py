# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# Любое действие выводит сумму денег
import decimal


def refill(r):
    while True:
        a = decimal.Decimal(input('Enter refill account: '))
        if a < 50 or a % 50 != 0:
            continue
        else:
            r = r + a
        return r


def take_off(t):
    LOW_LIMIT = decimal.Decimal(30)
    HI_LIMIT = decimal.Decimal(600)

    while True:
        a = decimal.Decimal(input('Enter take off account: '))
        p = a / 100 * decimal.Decimal(1.5)
        j = t
        if p < 30:
            t = t - a - LOW_LIMIT
            if t < 0:
                t = j
                print('Insufficient funds!!!')

        elif p > 600:
            t = t - a - HI_LIMIT
            if t < 0:
                t = j
                print('Insufficient funds!!!')

        else:
            t = t - a - p
            if t < 0:
                t = j
                print('Insufficient funds!!!')

        return t


menu = """
1. Refill account
2. Take off account
3. Exit
"""


def menus():
    money = 0
    count = 0
    while True:
        print(menu)
        if money > 5000000:
            money -= money / 10
        if count % 3 == 0:
            money += decimal.Decimal(money / 100) * 3
        print(f'Money = {money}\n')
        choice = int(input('Enter action: '))

        match choice:

            case 1:
                money = refill(money)
                count += 1
            case 2:
                money = take_off(money)
                count += 1
            case 3:
                break


menus()

