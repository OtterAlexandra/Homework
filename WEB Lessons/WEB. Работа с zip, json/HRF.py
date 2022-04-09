import math
import os


def human_read_format(size):
    if size == 0:
        return '0Б'
    else:
        pwr = math.floor(math.log(size, 1024))
        s = ["Б", "КБ", "МБ", "ГБ", "ТБ", "ПБ", "ЭБ", "ЗБ", "ЙБ"]
        if size > 1024 ** (len(s) - 1):
            return "я хз :3"
        return f"{size / 1024 ** pwr:.0f}{s[pwr]}"


def get_files_sizes():
    all = os.listdir(os.getcwd())
    result = list()
    for i in all:
        if os.path.isfile(i):
            size = human_read_format(os.stat(i).st_size)
            res = f'{i} {size}'
            result += [res]
    return '\n'.join(result)


print(get_files_sizes())
