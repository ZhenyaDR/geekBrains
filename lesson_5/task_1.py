def odd_nums(number):
    for num in range(1, number + 1):
        if num % 2 != 0:
            yield num


list_of_numbers = odd_nums(int(input("Число: ")))

print(next(list_of_numbers))
print(next(list_of_numbers))
print(next(list_of_numbers))
