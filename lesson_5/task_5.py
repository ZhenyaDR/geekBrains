src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 33]

unique_numbers = set()
unique_numbers_without_sort = []

for number in src:
    if number in unique_numbers:
        continue

    unique_numbers.add(number)
    if number in unique_numbers_without_sort:
        unique_numbers_without_sort.remove(number)
        continue

    unique_numbers_without_sort.append(number)

print(unique_numbers)
print(unique_numbers_without_sort)
