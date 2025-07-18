score=int(input("Enter a Number : "))

if score>=101:
    print("Verify Your Grade Again")
    exit()
elif score >=90:
    grade = "A"
elif score >=80:
    grade = "B"
elif score >=70:
    grade = "C"
elif score >=60:
    grade = "D"
else:
    grade ="E"

print("Grade : ",grade)
