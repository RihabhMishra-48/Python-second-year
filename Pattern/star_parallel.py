row=int(input("enter the number of rows: "))
col=int(input("enter the number of columns: "))
for i in range(row):
    for j in range(col):
        if (j==0 or j==col-1 ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()