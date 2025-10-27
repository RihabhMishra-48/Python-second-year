arr = [3, -1, 4]
n = len(arr)
total = 0

for i in range(n):
    total += arr[i] * (i + 1) * (n - i)

print(total)
