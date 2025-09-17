
n = int(input().strip())

eligible_count = 0


for _ in range(n):
    marks, attendance = map(int, input().split())
    if marks >= 75 and attendance >= 80:
        eligible_count += 1


print(eligible_count)
