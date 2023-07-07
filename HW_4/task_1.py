# 1. Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s
# (кроме переменной из одной буквы s) на None. Значения не удаляются,
# а помещаются в одноимённые переменные без s на конце.
datas = [42, -73, 12, 85, -15, 2]
s = 'Hello world!'
names = ('NoName', 'OtherName', 'NewName')
sx = 42


def global_f():
    g = globals()
    permutation = {}
    for name, value in g.items():
        if name.endswith('s') and len(name) > 1:
            permutation[name[:-1]] = g[name]
            g[name] = None

    for name, value in permutation.items():
        g[name] = value


global_f()
print(datas)
print(s)
print(names)
print(sx)
print(data)
print(name)

