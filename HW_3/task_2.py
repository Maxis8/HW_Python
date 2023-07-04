# 2. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

# Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.

my_lst = [11, 11, 12, 12, 6, 2, 4, 6, 2, 8, 10, 8, 4, 14, 14, 44, 44, 99, 6, 99]
print(my_lst)
count = 1
lst = []
for i in (my_lst):
    if i not in lst:
        if my_lst.count(i) > count:
            lst.append(i)
print(lst)
# Alternative
lst = [i for i in my_lst if my_lst.count(i) > 1]
print(my_lst)
print(set(lst))

