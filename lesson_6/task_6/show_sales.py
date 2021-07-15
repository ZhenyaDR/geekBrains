import sys

with open('bakery.csv', 'r', encoding='utf-8') as file:
    length = len(sys.argv)

    if length == 1:
        print(file.read())
    elif length == 2:
        start_position = int(sys.argv[1]) - 1
        for row in file.readlines()[start_position:]:
            print(row)
    elif length == 3:
        start_position = int(sys.argv[1]) - 1
        stop_position = int(sys.argv[2])
        for row in file.readlines()[start_position:stop_position]:
            print(row)

