minute = 60
hour = 3600
day = 216000
month = 6480000
year = 77760000

duration = int(input('Введите промежуток времени: '))

if duration < minute:
    print(f"{duration} сек")
elif duration < hour:
    print(f"{duration // minute} мин "
          f"{duration % minute} сек")
elif duration < day:
    print(f"{duration // hour} час "
          f"{duration % hour // minute} мин "
          f"{duration % minute} сек")
elif duration < month:
    print(
        f"{duration // day} день "
        f"{duration % day // hour} час "
        f"{duration % day % hour // minute} мин "
        f"{duration % minute} сек")
elif duration < year:
    print(
        f"{duration // month} месяц "
        f"{duration % month // day} день "
        f"{duration % month % day // hour} час "
        f"{duration % month % day % hour // minute} мин "
        f"{duration % minute} сек")
else:
    print(
        f"{duration // year} год "
        f"{duration % year // month} месяц "
        f"{duration % year % month // day} день "
        f"{duration % year % month % day // hour} час "
        f"{duration % year % month % day % hour // minute} мин "
        f"{duration % minute} сек")
