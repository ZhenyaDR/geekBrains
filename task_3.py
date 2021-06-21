input_number = int(input('Задайте число: '))

if input_number // 10 == 0 and input_number in [2, 3, 4]:
    print(f'{input_number} процента')
elif input_number == 1:
    print(f'{input_number} процент')
else:
    print(f'{input_number} процентов')
