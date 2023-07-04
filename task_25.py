size = 123
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    print(f.truncate(size))