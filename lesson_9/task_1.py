import time


class TrafficLight:
    __color = ''

    def running(self):
        while True:
            self.__color = 'Красный'
            print(self.__color)
            time.sleep(7)
            self.__color = 'Желтый'
            print(self.__color)
            time.sleep(2)
            self.__color = 'Зеленый'
            print(self.__color)
            time.sleep(3)


new_traffic_light = TrafficLight()
new_traffic_light.running()

