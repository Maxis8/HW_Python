# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

import csv
import json
from random import randint

myList = [{'lesson': 'Informatics'},
          {'lesson': 'Physics'},
          {'lesson': 'Mathematics'},
          {'lesson': 'Chemistry'}]

with open("filename.csv", 'w', newline='', encoding='utf-8') as file:
    csv_write = csv.DictWriter(file, fieldnames=[*myList[0]])
    csv_write.writeheader()
    csv_write.writerows(myList)


class DesClass:

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):

        if not (value.isalpha() and value[0].isupper()):
            raise TypeError("Only letter in name, first title")
        else:
            setattr(instance, self.name, value)


class Student:
    name = DesClass()
    last_name = DesClass()
    father_name = DesClass()

    def __init__(self, name: str, last_name: str, father_name: str, *args, **kwargs):
        self.name = name
        self.last_name = last_name
        self.father_name = father_name
        self._myList = self.lessons()
        self.performance = self.all_rating()
        self.add_json()

    def lessons(self):
        with open("filename.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            lst = []
            for row in reader:
                lst.append(row["lesson"])
        return lst

    def all_rating(self):
        gradeDict = {}
        for i in self._myList:
            x = randint(2, 5)
            y = randint(2, 5)
            z = randint(2, 5)
            iTest = randint(20, 100)
            gradeDict[
                i] = f"{x}, {y}, {z}    average rating - {round((x + y + z) / 3, 2)},    final certification - {iTest}"
        return gradeDict

    # вывод на экран в читабельном виде
    def on_display(self):
        print("©" * 100)
        print(f'{self.last_name} {self.name[0]}. {self.father_name[0]} ')
        print(" " + ';\n '.join([f'{key.capitalize()}: {value}' for key, value in self.performance.items()]))

    # сохраняем объект в Json
    def add_json(self):
        with open("students.json", 'a', encoding='utf-8') as json_f:
            json.dump(self.__dict__, json_f, indent=4, ensure_ascii=False)


p1 = Student("Алексей", "Синицын", "Викторович")
p2 = Student("Олег", "Смолов", "Сергеевич")
p3 = Student("Петр", "Стогов", "Константинович")

p1.on_display()
p2.on_display()
p3.on_display()

