n = int(input())  
ids = list(map(int, input().split()))

even_ids = []  
for student_id in ids:
    if student_id % 2 == 0:
        even_ids.append(student_id)

if even_ids:  
    print(*even_ids)
else:
    print(-1)
