num=int(input("enter the number: "))

for i in range(num):
    for j in range(num-i):
        print("*", end="")
    for j in range(i):
       print("  ", end="")
    for j in range (num-i):
        print("*", end="")
    print()