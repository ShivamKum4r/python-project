# age = int(input("Enter Age: "))
# day = str(input("Enter Day: ")).strip().capitalize()

# price = 12

# if day == "Wednesday":
#     if age >= 18:
#         price = price - 2
#         print("Price : $", price)
#     else:
#         print("Price : $", 6)
# elif age >= 18:
#     print("Price : $", price)
# else:
#     print("Price : $", 8)

age = int(input("Enter Age: "))
day = input("Enter Day: ").strip().capitalize()  # Normalize input

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price -= 2

print("Price : $", price)

    