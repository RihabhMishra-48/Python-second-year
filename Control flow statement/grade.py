

percentage = float(input("Enter your percentage: "))

if percentage < 25:
    grade = "D"
elif percentage >= 25 and percentage < 45:
    grade = "C"
elif percentage >= 45 and percentage < 65:
    grade = "B"
elif percentage >= 65 and percentage < 85:
    grade = "A"
else:
    grade = "A+"

print("Your grade is:", grade)
