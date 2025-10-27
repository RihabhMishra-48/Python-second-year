#Write a program to print all the natural numbers from 1 to N. Then print the same in reverse order.

num=int(input("Enter a number: "))
for i in range(1, num+1):
    print(i, end=" ")
for i in range(num, 0, -1):
    print(i, end=" ")