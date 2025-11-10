array=list(map(int,input("Enter numbers separated by space: ").split()))
B = 10
count = 0

for i in range(len(array)):
    sum_ = 0
    for j in range(i, len(array)):
        sum_ += array[j]
        if sum_ < B:
            count += 1

print(count)
