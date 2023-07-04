text = ['The biggest room in the apartment is the living room.',
        'This is where we watch TV in the evening, my little brother plays videogames there.',
        'My parents’ room is also big, and they have their own TV']
with open('new_data.txt', 'w', encoding='utf-8') as f:
    print(f.tell())
    for line in text:
        f.write(f'{line}\n')
        print(f.tell())
    print(f.tell())
print(f.tell())