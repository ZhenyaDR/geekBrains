class Stationary:
    _title = ''

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):
    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationary):
    def draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationary):
    def draw(self):
        print('Запуск отрисовки маркером')


stationary = Stationary()
stationary.draw()

pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

marker = Handle()
marker.draw()
