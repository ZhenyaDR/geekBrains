result_list = []
current_sum_of_element = 0

for i in range(1, 1001):
    if i % 2 == 0:
        continue
    cube_sum = i ** 3
    cube_sum_copy = cube_sum

    while cube_sum_copy != 0:
        current_sum_of_element += cube_sum_copy % 10
        cube_sum_copy //= 10

    if current_sum_of_element % 7 == 0:
        result_list.append(cube_sum)

    current_sum_of_element = 0

for index, element in enumerate(result_list):
    element_copy = element + 17

    while element_copy != 0:
        current_sum_of_element += element_copy % 10
        element_copy //= 10

    if current_sum_of_element % 7 == 0:
        result_list[index] = element + 17
    else:
        result_list.remove(element)

    current_sum_of_element = 0

print(result_list)
