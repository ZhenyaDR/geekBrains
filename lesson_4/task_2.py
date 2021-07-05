from requests import get, utils


def currency_rates(currency_param):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')

    list_of_currencies = {}
    encoding = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encoding)

    for string in content.split('Valute ID="')[1:]:
        currency_code = string.split('"')[1].split('CharCode>')[1].replace('</', '')
        currency_value = string.split('"')[1].split('Value>')[1].replace('</', '').replace(',', '.')
        currency_name = string.split('"')[1].split('Name>')[1].replace('</', '')
        list_of_currencies[currency_code] = {
            'char_code': currency_code,
            'name': currency_name,
            'value': currency_value,
        }
    return list_of_currencies.get(currency_param)


code = input('Введите название валюты: ').upper()

currency_result = currency_rates(code)

if currency_result is not None:
    print(f'{float(currency_result.get("value"))}')
else:
    print(None)
