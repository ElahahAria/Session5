print(" Welcome! You can create your own chess board with me!")

row=int(input("Enter the number of rows: "))
column=int(input("Enter the number of columns: "))

def Chess_board(column,row):
    
    for i in range(row):
        for j in range(column):
            if (i+j)%2==0 :
                print("#",end="")
            else:
                print("*",end="")
        print()

Chess_board(row,column)
