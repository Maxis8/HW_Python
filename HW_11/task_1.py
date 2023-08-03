# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
# Создайте класс Матрица. Добавьте методы для: вывода на печать, проверку на равенство, сложения, *умножения матриц

class Matrix:
    """Class Matrix"""
    def __init__(self, matrix):
        """Конструктор

        """
        self.matrix = matrix



    def __eq__(self, other):
        """Сравнение матриц .
        """
        return True if self.matrix == other.matrix else False

    def __add__(self, other):
        """Сложение матриц.
        Складывать матрицы можно, если у них одинаковое количество рядов и столбцов.

        """
        if len(self.matrix) != len(other.matrix):
            raise ValueError("incorrect matrix size")
        for row in range(len(self.matrix)):
            if len(self.matrix[row]) != len(other.matrix[row]):
                raise ValueError("incorrect matrix size")
        new_matrix = []
        for row_self, row_other in zip(self.matrix, other.matrix):
            new_matrix.append([*map(lambda x: sum(x), zip(row_self, row_other))])
        return Matrix(new_matrix)

    def __mul__(self, other):
        """Умножать матрицы можно, если количество столбцов первой матрицы совпадает с количеством строк во второй.
        """
        if len(self.matrix[0]) == len(other.matrix):
            new_matrix = []
            for row_self in self.matrix:
                temp = []
                for col_other in zip(*other.matrix):
                    temp.append(sum(map(lambda x: x[0] * x[1], zip(row_self, col_other))))
                new_matrix.append(temp)
            return Matrix(new_matrix)
        raise ValueError("incorrect matrix size")

    def __str__(self):
        """ Вывод матрицы."""
        result = ''
        for row in self.matrix:
            for elem in row:
                result += ''.join(f'{elem}\t')
            result += ''.join('\n')
        return result

matrix_1 = [[1, 2, 3],
            [2, 3, 1],
            [3, 1, 2]]
matrix_2 = [[3, 1, 2],
            [1, 2, 3],
            [2, 3, 1]]
m1 = Matrix(matrix_1)
m2 = Matrix(matrix_2)
print(m1 == m2)
m3 = m1 + m2
m4 = m1 * m2
print(m3)
print(m4)
print(Matrix.__doc__)
help(Matrix)

