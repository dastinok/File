import random

def key_gen():
    keylist = random.choice('abcdefghijklmnopqrstuvwxyz')
    return keylist

number = 0
list_item = ''
while number < 7:
    number = number + 1
    list_item = list_item.title() + key_gen()

print(list_item)