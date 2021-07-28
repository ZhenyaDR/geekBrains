class Worker:
    name = ''
    surname = ''
    position = ''
    _income = []

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return format(f'Имя сотрудника: {self.surname} {self.name}')

    def get_total_income(self):
        return f'Зарплата сотрудника: {self._income.get("wage") + self._income.get("bonus")}'


position_1 = Position('Иван', 'Иванов', 'Стажер', {'wage': 500, 'bonus': 300})

print(position_1.get_full_name())

print(position_1.get_total_income())

