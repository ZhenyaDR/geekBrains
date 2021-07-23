def type_logger(func):
    def wrapper(*args):
        for argument in args:
            print(f'{argument}: {type(argument)}')
        return func(*args)

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


print(calc_cube(15))
