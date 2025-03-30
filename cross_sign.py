from random import *
count=randint(11,13)
print(f'count= {count}')
p=0
q=count-4
t=1
r=count//2
for i in range(1,count):
    if i==1:
        for j in range(1,count+1):
            print("*",end='')
    if i==2:
        print("*",end='')
        print("*",end='')
        for l in range(q):
            print(" ",end='')
        print("*",end='')
        print("*",end='')
    if i>2 and i<=r:
        print("*",end='')
        for k in range(p):
            print(" ",end='')
        print("*",end='')
        for l in range(q):
            print(" ",end='')
        print("*",end='')
        for m in range(p):
            print(" ",end='')
        print("*",end='')
    if i==r+1:
        print("*",end='')
        for k in range(p):
            print(" ",end='')
        print("*",end='')
        for m in range(p):
            print(" ",end='')
        print("*",end='')
    if i>r+1:
        print("*",end='')
        for k in range(p):
            print(" ",end='')
        print("*",end='')
        for l in range(t):
            print(" ",end='')
        print("*",end='')
        for m in range(p):
            print(" ",end='')
        print("*",end='')
    if i>=r+1:
        p=p-1
    if i>r+1:
        t=t+2
    if i>=2 and i<=r:
        p=p+1
        q=q-2
    print()
for j in range(1,count+1):
    print("*",end='')