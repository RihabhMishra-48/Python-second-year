a=input("Enter a number: ")
n=int(a)
i=1
while i<=n:
    if n % i == 0:
        print(i)
    i += 1
