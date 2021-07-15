
dictionary = []

with open('logs.txt', 'r', encoding="utf-8") as f:
    for row in f:
        array_values = row.split(' ')
        dictionary.append((array_values[0], array_values[5].strip('"'), array_values[6]))

print(dictionary)



