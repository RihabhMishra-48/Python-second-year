rows = 5
num = 1

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if j % 2 != 0:      # odd position → number
            print(num, end=" ")
            num += 2        # next odd number
        else:               # even position → '*'
            print("*", end=" ")
    print()
