list_names = ["Иван", "Мария", "Петр", "Илья", "Тест", "тестерович"]


def accepted(word, letter):
    return word.lower().startswith(letter.lower())


def thesaurus(names):
    dictionary = {}
    for el in names:
        word = el[0].title()
        dictionary[word] = [element for element in names if accepted(element, el[0])]
    print(dictionary)


thesaurus(list_names)
