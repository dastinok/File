'''✔ Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла,
возвращайтесь в его начало.'''

def get_file(new_file):
    massive_mult = []
    names = []
    len_massive_mult = 0
    len_names = 0

    with (
        open('num_2.txt', 'r', encoding='utf-8') as f1,
        open('file.txt', 'r', encoding='utf-8') as f2,
        open(new_file, 'w', encoding='utf-8') as f3
    ):
        while numbers := f1.readline():
            first_num, second_num = numbers.strip().split('||')
            massive_mult.append(int(first_num) * float(second_num))
            len_massive_mult += 1
        while name := f2.readline():
            names.append(name[:-1])
            len_names += 1

        lengths = sorted([len_massive_mult, len_names])

        for i in range(lengths[0]):
            if massive_mult[i] < 0:
                f3.write(names[i].lower() + ' ' + str(abs(massive_mult[i])) + '\n')
            else:
                f3.write(names[i].upper() + ' ' + str(round(massive_mult[i])) + '\n')
        for i in range(lengths[1] - lengths[0]):
            if massive_mult[i] < 0:
                f3.write(names[i].lower() + ' ' + str(abs(massive_mult[i])) + '\n')
            else:
                f3.write(names[i].upper() + ' ' + str(round(massive_mult[i])) + '\n')

get_file('seminar_3.txt')