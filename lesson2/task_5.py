price_list = [57.8, 46.51, 97, 15.24, 91.4, 100, 204.99, 20.5, 15.01, 90]

for price in price_list:
    ruble = int(price)
    print(f'{ruble} руб {round((price - ruble) * 100):02d} коп', end=', ')
print()

old_list_id = id(price_list)
price_list.sort(), print(price_list)

print(old_list_id == id(price_list))

new_reversed_list = sorted(price_list, reverse=True)
print(new_reversed_list), print(sorted(new_reversed_list[:5]))
