# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей
# в задаче выше. Проверяйте различные случайные варианты и выведите 4 успешных расстановки.
# *Выведите все успешные варианты расстановок
import random
Q = 8


def eight_queens(position: list[list[int]]) -> bool:
    for num, item in enumerate(position):
        for item2 in position[num + 1:]:
            if item[0] == item2[0] or item[1] == item2[1] or abs(item[0] - item2[0]) == abs(item[1] - item2[1]):
                return False
    return True


def count_true_position(print_counter):
    position = []
    count = 1
    counter = 0

    while count <= print_counter:
        counter += 1

        while len(position) < Q:
            lst = [random.randint(1, Q) for _ in range(2)]
            if lst not in position:
                position.append(lst)

        if eight_queens(position):
            print(position, 'iter = ', counter)
            count += 1
        position.clear()

