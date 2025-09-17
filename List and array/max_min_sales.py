n = int(input())  
sales = list(map(int, input().split()))
max=0
min=0
for sale in sales:
    if sale>max:
        max=sale
    if sale<min or min==0:
        min=sale
print(max,min)