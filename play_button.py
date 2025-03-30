from random import *
count = randint(9, 15)
print(f'count: {count}')
def print_button(character, count):
    for i in range(1, count):
        for j in range(i):
            print(character, end = ' ')
        print()
    for i in range(count, 0, -1):
        for j in range(i):
            print(character ,end = ' ')
        print()
print_button("*", count)