def val_checker(check_func):
    def _val_checker(func):
        def main_func(*args):
            if check_func(args[0]) is False:
                raise ValueError(f'wrong value: {args[0]}')
            return func(*args)

        return main_func

    return _val_checker


@val_checker(lambda x: x >= 6)
def calc_cube(x):
    return x ** 3


print(calc_cube(6))
