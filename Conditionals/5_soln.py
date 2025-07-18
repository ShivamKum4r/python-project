weather=str(input("Enter Weather : ")).strip().capitalize()
if weather == "Sunny":
    activity="Go For Walk"
elif weather == "Rainy":
    activity = "Read a Book"
elif weather == "Snowy":
    activity= "Build a Snowman"
else :
    activity ="Do Your Task"
print("Activity :",activity)
