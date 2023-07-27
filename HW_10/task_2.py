# Возьмите 1-3 любые задачи из прошлых семинаров, которые вы уже решали. Превратите функции в методы класса.
# Задачи должны решаться через вызов методов экземпляра.
import json
import csv
import json
import csv


class Converter:
    def __init__(self, file_csv, file_json):

        self.file_csv = file_csv
        self.file_json = file_json

    def csv_convert_jason(self):
        with open(self.file_csv, 'r', newline='', encoding='utf-8') as f1:
            csv_file = csv.reader(f1)
            lst = []
            for i, (level, id_, name) in enumerate(csv_file):
                if i:
                    lst.append({'level': level, 'id_': id_.zfill(10), 'name': name.capitalize(),
                                'hash': hash(id_ + name)})
        with open(self.file_json, 'w', encoding='utf-8') as f2:
            json.dump(lst, f2, indent=4)


ex = Converter('task2.csv', 'task2_convert.json')
ex.csv_convert_jason()

