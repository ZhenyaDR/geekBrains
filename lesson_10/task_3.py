class Cell:
    __count: int

    def __init__(self, count):
        if count < 0:
            raise ValueError('Число должно быть положительным')
        self.__count = count

    def __str__(self):
        return f'{self.__count}'

    def __add__(self, other: 'Cell'):
        return Cell(self.__count + other.__count)

    def __sub__(self, other: 'Cell'):
        if self.__count < other.__count:
            raise ValueError('Ячеек во второй клетке больше, чем в первой')
        return Cell(self.__count - other.__count)

    def __mul__(self, other: 'Cell'):
        return Cell(self.__count * other.__count)

    def __floordiv__(self, other: 'Cell'):
        return Cell(self.__count // other.__count)

    def make_order(self, length):
        row = '*' * length + '\n'
        result = row * (self.__count // length)
        if self.__count % length:
            result += '*' * (self.__count % length)
        return result


cell_first = Cell(14)
cell_second = Cell(7)

print(cell_first.make_order(6))
