text = 'We live on the second floor, so usually we do not use the elevator. There are four rooms in the apartment – my ' \
       'parents’ room, my little brother’s room, the room where I live, and the living room. There are also, of course, ' \
       'a cozy kitchen and a bathroom.'
with open('new_data.txt', 'a', encoding='utf-8') as f:
    res = f.write(text)
    print(f'{res = }\n{len(text) = }')