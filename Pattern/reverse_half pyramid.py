num = int(input("Enter number of rows: "))

for i in range(1, num+1):         
    for k in range(i):
        print(" ", end=" ")
    for j in range(num - i):
        print("*", end=" ")
    
    
    print()   