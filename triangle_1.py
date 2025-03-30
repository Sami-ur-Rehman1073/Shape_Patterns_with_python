from random import *
rows=randint(5,10)
for i in range(1,rows+1):
    for j in range(i):
        print("*",end='')
    print()