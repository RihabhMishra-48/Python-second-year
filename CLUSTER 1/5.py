def find_max(arr):
    return max(arr)

N = int(input("Enter size of array: "))
arr = []

for i in range(N):
    arr.append(int(input()))

print(find_max(arr))
