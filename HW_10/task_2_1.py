# Возьмите 1-3 любые задачи из прошлых семинаров, которые вы уже решали. Превратите функции в методы класса.
# Задачи должны решаться через вызов методов экземпляра.
from random import randint


class Roulette:

    def __init__(self, start, end, attempts):

        self.start = start
        self.end = end
        self.attempts = attempts

    def get_num(self):
        x = randint(self.start, self.end)
        return x

    def guess_num(self):
        rand_num = self.get_num()
        while self.attempts > 0:
            self.attempts -= 1
            user_num = int(input('Enter number: '))

            if user_num == rand_num:

                return print('You win')
            else:
                if user_num < rand_num:
                    print('<')
                else:
                    print('>')

                continue

        else:
            print(rand_num)
            return print('You lose...')


us = Roulette(1, 50, 3)
us.guess_num()

