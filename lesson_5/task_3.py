tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Вася', 'Таня', 'Олег'
]
classes = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def generate(tutors_list, classes_list):
    for index, tutor in enumerate(tutors_list):
        yield (tutor, classes_list[index] if 0 <= index < len(classes_list) is not None else None)


result = generate(tutors, classes)

for _ in tutors:
    print(next(result))
