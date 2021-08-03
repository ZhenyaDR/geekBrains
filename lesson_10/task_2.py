from abc import abstractmethod, ABC


class Clothes(ABC):
    total = 0

    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        if self.__size < 0:
            return ValueError('Invalid value size')
        return self.__size

    @abstractmethod
    def get_size_of(self):
        pass


class Suite(Clothes):
    def get_size_of(self):
        _h = self.size
        sum = float(f'{_h * 2 + 0.3 :0.2f}')
        Clothes.total += sum
        return sum


class Coat(Clothes):
    def get_size_of(self):
        size = self.size
        sum = float(f'{size / 6.5 + 0.5 :0.2f}')
        Clothes.total += sum
        return sum


coat = Coat(15)
print(coat.get_size_of())

suite = Suite(4.5)
print(suite.get_size_of())

print(Clothes.total)
