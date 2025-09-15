array=list(map(int,input("Enter number separated by space: ").split()))
num=int(input("Enter the number to be checked: "))
count=0 
for i in array:
    if i==num:
        count+=1
print(count)