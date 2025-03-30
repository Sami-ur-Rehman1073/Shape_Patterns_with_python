def print_trapezium(character,rows,columns):
    for i in range(rows):
        for k in range(i):
            print(" ",end='')
        for j in range(columns):
            print("*",end=' ')
        print()
    
print_trapezium("*",9,7)