'''✔ Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.'''

import random

with open('file.txt', 'a', encoding='utf-8') as f:

    def get_alpha():

        key_list = random.choice('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
        return key_list

    number = 0
    list_item = ''
    while number < 7:
        number = number + 1
        list_item = list_item.title() + get_alpha()

    print(f.write(list_item))
    print(f.write('\n'))


    print(list_item)