# 5. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)
print(num)
count = 0
while count < 10:
    player_num = int(input('Enter number 0 - 1000: '))
    if player_num < num:
        print('You enter < number')
    elif player_num > num:
        print('You enter > number')
    else:
        print('BINGO!!! YOU WIN!!!')
        break
    count += 1
    print('Use attempts: ', count, '\n')
else:
    print('You loose....')

