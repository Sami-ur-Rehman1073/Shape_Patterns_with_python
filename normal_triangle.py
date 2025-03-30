from random import *
rows=randint(5,10)
print(f'Rows:{rows}')
p=rows*2
q=1
for i in range(1,rows+1):
    for j in range(p):
        print(" ",end='')
    p=p-1
    for k in range(q): 
        print("*",end='')
    q=q+2 
    print() 