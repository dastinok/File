'''✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.'''

import random
from random import randint, sample, randbytes
from string import ascii_letters
import os

def rand_ext(list_ext: list[str]) -> str:
    return random.choice(list_ext)


def create_file(extension: list[str], dir: str, len_name: int = 6, maxim_name: int = 30, min_byte: int = 256,
                max_byte: int = 4096, amount_files: int = 5):
    for _ in range(amount_files):
        name_size = randint(len_name, maxim_name)
        ext = rand_ext(extension)
        #file_name = ''.join(sample(ascii_letters, name_size)) + '.' + ext
        file_name = 'asdfg.txt'
        if not os.path.exists(dir):
            os.mkdir(dir)
        full_name = os.path.join(dir, file_name)
        if os.path.exists(full_name):
            full_name = os.path.join(dir, file_name.split('.')[0] + '_1' + '.' + ext)

        with open(full_name, 'ab') as file:
            size = randint(min_byte, max_byte)
            result = randbytes(size)
            file.write(result)


create_file(['txt', 'doc', 'md', 'rtf'], dir = 'test', amount_files = 3)