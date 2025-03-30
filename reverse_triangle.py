from random import *
rows=randint(5,10)
print("rows: ",rows)
for i in range(rows,0,-1):
    for j in range(i):
        print("*",end='')
    print()