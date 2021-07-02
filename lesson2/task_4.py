persons_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for person in persons_list:
    name = person.split().pop().lower().title()
    print(f'Привет, {name}!')
