arr=list(map(int, input("Enter numbers separated by space: ").split()))
for num in arr:
    if num<0:
        print( num)
    else:
        print("No negative number found")
        
    