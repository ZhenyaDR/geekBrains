import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(number):
    list_of_jokes = []
    for count in range(0, number):
        list_of_jokes.append(f"{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}")
    print(list_of_jokes)


get_jokes(int(input('Введите число: ')))
