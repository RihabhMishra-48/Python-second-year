arr=list(map(int,input("Enter numbers separated by space: ").split()))
max_value=0
for num in arr:
    if num > max_value:
        max_value = num
print(max_value)