'''✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.
'''
import random

def get_new_file(amount_strings, file_name):

    for _ in range(amount_strings): # Перебор по строке
        outfile = open(file_name, 'a')
        first_num = random.randrange(-1000, 1000)
        second_num = random.uniform(-1000.00, 1000.00)
        print(first_num)
        print(second_num)

        outfile.write(str(first_num))
        outfile.write('  ||  ')
        outfile.write(str(second_num))
        outfile.write('\n')
        outfile.close()
        print('Данные записаны')


print(get_new_file(5,'num_2.txt'))