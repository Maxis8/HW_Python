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
        return f'{self.name}: Глубина обитания: {self.depth}'


class Bird(Animals):
    def __init__(self, name, wings):
        super().__init__(name)
        self.wings = wings

    def unique_info(self):
        return f' {self.name}: Размах крыльев: {self.wings}'


class Mammal(Animals):

    def __init__(self, name, coat):
        super().__init__(name)
        self.coat = coat

    def unique_info(self):
        return f'{self.name}: Размах крыльев: {self.coat}'


class AnimalFactory:
    @staticmethod
    def new_animal(animal_type, name, *args):
        if animal_type == 'Fish':
            return Fish(name, *args)
        elif animal_type == 'Bird':
            return Bird(name, *args)
        elif animal_type == 'Mammal':
            return Mammal(name, *args)
        else:
            return Animals(name)


new_mammal = AnimalFactory.new_animal('Mammal', 'Bear', 10)
print(new_mammal.__dict__)

