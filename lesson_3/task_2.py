NUMBER_DICTIONARY = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                     'seven': 'семь', 'eight': 'восемь',
                     'nine': 'девять', 'ten': 'десять'}


def num_translate(number):
    if number.istitle():
        print(NUMBER_DICTIONARY.get(number.lower()).title())
    else:
        print(NUMBER_DICTIONARY.get(number))


num_translate(input('Введите число от одного до десяти на английском:'))
