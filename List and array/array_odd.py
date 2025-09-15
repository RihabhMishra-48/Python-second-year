array=list(map(int,input("Enter numbers separated by space: ").split()))
odd_numbers=[num for num in array if num%2!=0]
print(odd_numbers)