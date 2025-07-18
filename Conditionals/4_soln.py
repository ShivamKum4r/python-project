fruit=str(input("Enter Fruit : ")).strip().capitalize()

if fruit == "Banana":
    colour=str(input("Enter Colour : ")).strip().capitalize()
    if colour == "Green":
        print("Unripe")
    elif colour == "Yellow":
        print("Ripe")
    elif colour == "Brown":
        print("Ovrripe")
else :
    print("Fruit info not available ")
    exit()
    