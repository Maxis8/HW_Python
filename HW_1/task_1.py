# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке
A = 11
edge = 6
for i in range(2, A):
    for j in range(2, edge):
        print(f'{j} x {i:>2d} = {j * i:>2d}', end='       ')
    print('   ')
print(' ')
edge = 10
for i in range(2, A):
    for j in range(6, edge):
        print(f'{j} x {i:>2d} = {j * i:>2d}', end='       ')
    print('   ')

