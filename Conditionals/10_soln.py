species=str(input("Emter Pet Species : ")).strip().capitalize()
age = int(input("Enter age of Pet : "))
food = None 
if species == "Dog":
    if age < 2 :
        food = "Puppy Food"
    else:
        food ="Senior Dog Food"
elif species == "Cat":
    if age > 5 :
        food = "Senior Cat Food"
    else:
        food = "Kitten Food"
else:
    print("Your Pet Food Recommendations not available ")
if food is not None:
    print(food,"is your Pet Food")