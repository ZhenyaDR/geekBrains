def currency_rates(currency_param):
    from requests import get, utils
    import datetime
    currency = currency_param.upper()
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')

    list_of_currencies = {}
    encoding = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encoding)

    parsed_date = content.split('Date="')[1:][0].split('"')[0]
    date = datetime.datetime.strptime(parsed_date, "%d.%m.%Y").strftime('%Y-%m-%d')

    for string in content.split('Valute ID="')[1:]:
        currency_code = string.split('"')[1].split('CharCode>')[1].replace('</', '')
        currency_value = string.split('"')[1].split('Value>')[1].replace('</', '').replace(',', '.')
        currency_name = string.split('"')[1].split('Name>')[1].replace('</', '')
        list_of_currencies[currency_code] = {
            'char_code': currency_code,
            'name': currency_name,
            'value': currency_value,
        }

    if currency in list_of_currencies:
        return f'{float(list_of_currencies[currency].get("value"))}, {date}'
    else:
        return None


if __name__ == '__main__':
    import sys
    exit(currency_rates(sys.argv[1]))
