# Due to an immense rise in Pollution, Kejriwal is back with the Odd and Even Rule in Delhi. The scheme
# is as follows, each car will be allowed to run on Sunday if the sum of digits which are even is divisible by
# 4 or the sum of digits which are odd in that number is divisible by 3. However, to check every car for the
# above criteria can't be done by the Delhi Police. You need to help Delhi Police by finding out if a car
N = int(input("Enter car number: "))

sum_even = 0
sum_odd = 0

for digit in str(N):
    d = int(digit)
    if d % 2 == 0:
        sum_even += d
    else:
        sum_odd += d

if sum_even % 4 == 0 or sum_odd % 3 == 0:
    print("Yes")
else:
    print("No")
