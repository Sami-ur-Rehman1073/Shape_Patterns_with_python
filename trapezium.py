rows=int(input("Enter rows: "))
columns=int(input("Enter columns: "))
p=rows*2
for i in range(1,rows+1):
    for k in range(p):
        print(" ",end='')
    if i==1:
        for j in range(1,columns+1):
           print("*",end='')
    if i>1 and i<rows:
        print("*",end='')
        for l in range(columns-2):
            print(" ",end='')
        print("*",end='') 
    if i==rows:
        for j in range(1,columns+1):
           print("*",end='')
    p=p-1
    print()