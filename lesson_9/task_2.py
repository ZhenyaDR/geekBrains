class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_asphalt_mass(self, weight, thickness):
        return int((self._length * self._width * weight * thickness) / 1000)


msk_road = Road(20, 5000)

print(f'{msk_road.calc_asphalt_mass(25, 5)} т')
