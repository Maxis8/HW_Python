# Доработаем задачи 5-6. Создайте класс-фабрику. Класс принимает тип животного (название одного из созданных классов) и
# параметры для этого типа. Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.


class Animals:
    def __init__(self, name):
        self.name = name


class Fish(Animals):
    def __init__(self, name, depth):
        super().__init__(name)
        self.depth = depth

    def unique_info(self):
        return f'Имя: {self.name}: Глубина обитания: {self.depth}'


class Bird(Animals):
    def __init__(self, name, wings):
        super().__init__(name)
        self.wings = wings

    def unique_info(self):
        return f'Имя: {self.name}: Размах крыльев: {self.wings}'


class Mammal(Animals):

    def __init__(self, name, coat):
        super().__init__(name)
        self.coat = coat

    def unique_info(self):
        return f'Имя: {self.name}: Длина шерсти: {self.coat}'


class AnimalFactory(Bird):
    def __init__(self, name, wings):
        super().__init__(name, wings)

    def new_animal(self):
        return self.name, self.wings


new_a = AnimalFactory('Crow', 0.9)
print(new_a.new_animal())
print(new_a.unique_info())
print(new_a.__dict__)

