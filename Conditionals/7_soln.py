order=input("Enter Order : ").strip().capitalize()
extra_shot_input = input("Do You Want Extra Shot (Yes/No) : ").strip().capitalize()
extra_shot = extra_shot_input == "Yes"

if  extra_shot:
    print(order + " Coffee With Extra Shot  ")
else:
    print(order + " Coffee")


# order = input("Enter Order: ").strip().capitalize()
# extra_shot_input = input("Do You Want Extra Shot (Yes/No): ").strip().lower()

# extra_shot = extra_shot_input == "yes"

# if extra_shot:
#     print(order + " Coffee With Extra Shot")
# else:
#     print(order + " Coffee")
