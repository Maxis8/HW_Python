# 2. Напишите функцию для транспонирования матрицы

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# Таблица
def print_matrix(m):
    for column in m:
        for row in column:
            print(row, "\t", end="")
        print()
    return ''


print_matrix(matrix)

print()
res = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
# res = [list(i) for i in zip(*matrix)]
print(print_matrix(res))

