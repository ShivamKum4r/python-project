age=int(input("Enter a Number : "))
if age<13:
    print("Children")
# elif age>=13 & age<20:
#     print("Teenager")
elif age<19:
    print("Teenager")
elif age<60:
    print("Adult")
else:
    print("Senior")