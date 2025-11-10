A = [1, 2, 3]
B = 5
good=0

for i in range(len(A)):
    sum_ = 0
    for j in range(i, len(A)):
        sum_ += A[j]
        length = j - i + 1

        if (length % 2 == 0 ) or (sum_ % 2 == 0 and sum_ < B) or (sum_ % 2 != 0 and sum_ > B):
            good += 1
            break 
    else:
        continue
    break

