import re


def email_parse(email):
    regex = r"^(?P<login>[A-Za-z0-9\-_.]+)@(?P<domain>[a-z]+.[a-z]{2,4}$)"
    pattern = re.compile(regex)

    if pattern.search(email) is None:
        raise ValueError(f' wrong email: {email}')

    for match in pattern.finditer(email):
        print(match.groupdict())


email_parse(input('Введите почту: '))
