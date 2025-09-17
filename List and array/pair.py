n = int(input().strip())
deadlines = list(map(int, input().split()))
k = int(input().strip())

count = 0
for i in range(n):
    for j in range(i+1, n):
        if deadlines[i] + deadlines[j] == k:
            count += 1

print(count)
