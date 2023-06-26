# 3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
while True:
    num = int(input('Enter number 2-100000: '))
    if 2 > num or num > 100000:
        print('Try again!!!: ')
    else:
        print(num)
        if num in (2, 3):
            print('Prime number!')
        else:
            edge = (num ** 0.5)
            for i in range(2, int(edge)+1):
                if num % i == 0:
                    print('Composite number!')
                    break
            else:
                print('Prime number!')
