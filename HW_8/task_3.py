# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных
# файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.
import os
import json
import csv
import pickle


def dir_size(dir_):
    total_size = 0
    for path, dirs, files in os.walk(dir_):
        for f in files:
            total_size += os.path.getsize(os.path.join(path, f))
    return total_size


def data_dir(direct):
    lst = []
    for path, dirs, files in os.walk(direct):
        for d in dirs:
            lst.append({'obj': d, 'parent': os.path.basename(path), 'obj_type': 'directory',
                        'size': dir_size(os.path.join(path, d))})
        for f in files:
            lst.append({'obj': f, 'parent': os.path.basename(path), 'obj_type': 'file',
                        'size': os.path.getsize(os.path.join(path, f))})

    if not os.path.exists('Files'):
        os.makedirs('Files')

    with open('Files/data.json', 'w', encoding='utf-8') as j, \
            open('Files/data.csv', 'w', newline='', encoding='utf-8') as c, \
            open('Files/data.pickle', 'wb') as p:

        json.dump(lst, j)

        wr_csw = csv.DictWriter(c, fieldnames=['obj', 'parent', 'obj_type', 'size'])
        wr_csw.writeheader()
        wr_csw.writerows(lst)

        pickle.dump(lst, p)


directory = os.getcwd()
data_dir(directory)
