# 1.Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
from os import path
from os import path
path_all = 'C:\Python\pythonw.exe\Files\info.txt'


def path_split(ph):
    p = path.basename(ph)
    ph = ph.replace(p, '')
    name, name1 = path.splitext(p)
    return ph, name, name1


print(*path_split(path_all))


