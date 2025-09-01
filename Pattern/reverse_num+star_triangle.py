num=int(input("enter the number: "))
for i in range(num, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(num-i):
    
        print("*", end="")
    for j in range(1,num-i):
    
        print("*", end="")
    
    print()