array=list(map(int,input("Enter numbers separated by space: ").split()))
num=int(input("enter the increament value: "))
new_array=[x+num for x in array]
print(new_array)