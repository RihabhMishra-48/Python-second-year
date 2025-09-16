
n = int(input().strip())


marks = list(map(int,input().split()))


passed = 0
failed = 0

for m in marks:
    if m >= 35:
        passed += 1
    else:
        failed += 1

print(passed, failed)

