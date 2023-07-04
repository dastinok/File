last = before = 0
text = ['The biggest room in the apartment is the living room.',
        'This is where we watch TV in the evening, my little brother plays videogames there.',
        'My parents’ room is also big, and they have their own TV']
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
        print(f'{last = }, {before = }')
    print(f'{last = }, {before = }')
    print(f'{f.seek(before, 0) = }')
    f.write('\n'.join(text))