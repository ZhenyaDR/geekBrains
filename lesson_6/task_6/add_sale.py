import sys

if len(sys.argv) != 2:
    exit(1)

with open('bakery.csv', 'a+', encoding='utf-8') as file:
    print(sys.argv[1], file=file)
    # file.write(f"{sys.argv[1]}\n")
