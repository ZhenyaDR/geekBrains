import os
import sys


def show_statistics(folder):
    result_array = {0: 0, 10: 0, 100: 0, 1000: 0, 10000: 0, 100000: 0}
    keys = [0, 10, 100, 1000, 10000, 100000]

    for root, dirs, files in os.walk(folder):
        for file in files:
            file_size = os.stat(os.path.join(root, file)).st_size
            if file_size == 0:
                result_array[0] += 1
                continue
            for index, key in enumerate(keys):
                if len(keys) == index + 1:
                    break
                if key <= file_size <= keys[index + 1]:
                    result_array[keys[index + 1]] += 1

    print(result_array)


if __name__ == '__main__':
    try:
        argument_folder = sys.argv[1]
    except IndexError as e:
        print('folder not defined as argument')
        exit(1)
    show_statistics(argument_folder)

