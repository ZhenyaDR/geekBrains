char_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
edited_list = []

for element in char_list:
    if element.isdigit():
        edited_list.extend(['":', f'{int(element):02d}', ':"'])
    elif element[1:].isdigit():
        edited_list.extend(['":', f'{element[0]}{int(element[1]):02d}', ':"'])
    else:
        edited_list.append(element)

print(' '.join(edited_list).replace(' :"', '"').replace('": ', '"'))
