class Matrix:
    def __init__(self, param):
        self.data = param

    def __str__(self):
        return '\n'.join(map(str, self.data))

    def __add__(self, other):
        result = []
        for element in range(len(self.data)):
            if len(other.data) > element:
                result.append([])
                for sub_elem in range(len(self.data[0])):
                    if len(other.data[element]) > sub_elem:
                        result[element].append(self.data[element][sub_elem] + other.data[element][sub_elem])
                    else:
                        result[element].append(self.data[element][sub_elem])
        return Matrix(result)


first = [[31, 22], [37, 43], [51, 86]]
second = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
third = [[3, 5, 8, 3], [8, 3, 7, 1]]

matrix_1 = Matrix(second)
matrix_2 = Matrix(third)

print(matrix_1 + matrix_2)
