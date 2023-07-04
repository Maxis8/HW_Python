# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# 1) Какие вещи взяли все три друга
# 2) Какие вещи уникальны, есть только у одного друга и имя этого друга
#
# 3) Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

hike = {'Иван': ('котелок', 'нож', 'спички', 'vodka', 'телефон' ),
        'Виктор': ('палатка', 'фонарик', 'продукты', 'шампуры', 'телефон'),
        'Карина': ('палатка', 'одеяло', 'телефон', 'нож', 'beer'),
        'Кристина': ('палатка', 'колонки', 'одеяло', 'телефон', 'boudoir', 'martini')
        }
print('\n'.join(f'{k} : {v}' for k, v in hike.items()))
s = ()
for v in hike.values():
    s += v
print(f'\nЭти вещи взяли все три друга: {set(s)}')

all_val = list(hike.values())
all_key = list(hike.keys())
all_list = []
for key in hike:
    all_list.extend(list(hike[key]))
for items in all_val:
    have_all = set(all_val[0]).intersection(set(items))
if have_all .intersection(set(items)) != set():
    print(f'Это есть у всех: {have_all}')
for i in range(len(all_val)):
    all_exclusive = set(all_val[i])
    for items in hike.values():
        if all_val.index(items) == i:
            continue
        all_exclusive = all_exclusive.difference(set(items))
    print(f'Эти вещи уникальны, есть только у одного друга:  {all_key[i]} {all_exclusive}')
deprived = set()
for i in range(len(all_val)):
    for key, value in hike.items():
        if all_list.count(value[i]) == len(hike) - 1:
            deprived.add(value[i])
for key, value in hike.items():
    for i in deprived:
        if i not in hike[key]:
            print(f'{key} не взял с собой {i}')

