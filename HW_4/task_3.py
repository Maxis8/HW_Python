# 3. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.


def to_swap(**kwargs):
    res = {}
    for key, value in kwargs.items():
        res[str(value)] = key

    return res


print(to_swap(name='Sam', lastname='Whiskey', age=20, friends=['msr. Daniels', 'sr. Jerez', 'm. Cognac ']))

