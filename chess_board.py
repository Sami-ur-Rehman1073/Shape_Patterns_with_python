def print_chess_board():
    count=int(input("Enter the count: "))
    p=0
    if count%2!=0:
        for n in range((count)):
            for i in range(3):
                for l in range(5):
                    for j in range(7):
                        print("*",end="")
                    for k in range(7):
                        print(" ",end="")
                print()
            if p>count-2:
                break
            for i in range(3):
                for l in range(5):
                    for j in range(7):
                        print(" ",end="")
                    for k in range(7):
                        print("*",end="")
                print()
            p=p+2

    if count%2==0:
        for n in range(count//2):
            for i in range(3):
                for l in range(5):
                    for j in range(7):
                        print("*",end="")
                    for k in range(7):
                        print(" ",end="")
                print()
            for i in range(3):
                for l in range(5):
                    for j in range(7):
                        print(" ",end="")
                    for k in range(7):
                        print("*",end="")
                print()

print_chess_board()      