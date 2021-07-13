def odd_nums(number):
    result = set()
    for num in range(1, number + 1):
        if num % 2 != 0:
            result.add(num)
    return result


list_of_numbers = odd_nums(int(input("Число: ")))

print(list_of_numbers)
