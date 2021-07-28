class Car:
    _speed = 0
    _color = 'Black'
    _name = 'car'
    _is_police = False

    def __init__(self, speed, color, name, is_police=False):
        self._name = name
        self._speed = speed
        self._color = color
        self._is_police = is_police

    def go(self):
        print('go')

    def stop(self):
        print('stop')

    def turn(self, direction):
        print(f'Повернули на {direction}')

    def show_speed(self):
        print(self._speed)


class TownCar(Car):
    __max_speed = 60

    def show_speed(self):
        super().show_speed()
        if self._speed > self.__max_speed:
            print(f'Вы превысили допустимую скорость в {self.__max_speed} км/ч')
        return self


class SportCar(Car):
    pass


class WorkCar(Car):
    __max_speed = 40

    def show_speed(self):
        super().show_speed()
        if self._speed > self.__max_speed:
            print(f'Вы превысили допустимую скорость в {self.__max_speed} км/ч')
        return self


class PoliceCar(Car):
    pass


town_car_first = TownCar(59, 'Red', 'Lada')
town_car_second = TownCar(99, 'Black', 'Toyota')

town_car_first.show_speed()
town_car_second.show_speed()


work_car_first = WorkCar(20, 'Red', 'Lada')
work_car_second = WorkCar(41, 'Black', 'Toyota')


work_car_first.show_speed().turn('право')
work_car_second.show_speed()
