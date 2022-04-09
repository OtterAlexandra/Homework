from zipfile import ZipFile, Path
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


with ZipFile('input.zip') as zip:
    for name in zip.namelist():
        file_path = Path('input.zip', name)
        items = name.rstrip("/").split("/")
        pop = zip.getinfo(name).file_size
        size = ''
        if file_path.is_file():
            size = human_read_format(pop)
        print("  " * (len(items) - 1) + items[-1] + ' ' + size)
