# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестирования возьмите pickle версию файла из предыдущей задачи. Функция должна извлекать ключи
# словаря для заголовков столбца из переданного файла.
import pickle
import csv


def pickle_convert_csv(file):
    with open(file, 'rb') as f1:
        lst = pickle.load(f1)
    my_dict = {}
    for dictionary in lst:
        for key, value in dictionary.items():
            my_dict.setdefault(key, []).append(value)

    with open('Tasks/task2_convert.csv', 'w', newline='', encoding='utf-8') as f2:
        wr_csv = csv.writer(f2, delimiter='|')
        wr_csv.writerow(my_dict.keys())
        wr_csv.writerows(zip(*my_dict.values()))


pickle_convert_csv('Tasks/task2_convert.pickle')

