
# ______________________________________________________________________slide 16
def printRecipe():
    print("1. Cook tortilla")
    print("2. Place cooked chicken onto tortilla.")
    print("3. Add your favorita salsa.")
    return("4. Enjoy!")

print(printRecipe())

def printRecipe(): # taco recipie
    print("1. Cook tortilla")
    print("2. Place cooked chicken onto tortilla.")
    print("3. Add your favorita salsa.")

    return("4. Enjoy!")

print(printRecipe())

def printRecipe(food):
    if (food == "taco"):
        print("1. Cook tortilla")
        print("2. Place cooked chicken onto tortilla.")
        print("3. Add your favorita salsa.")
    if (food == "ice cream"):
        print("1. Grab a bowl, spoon, your favorite ice cream, and toppings.")
        print("2. Scoop favorite ice cream flavor into bowl.")
        print("3. Add toppings.")
    return("4. Enjoy!")

print(printRecipe("ice cream"))

def printRecipe(meal, desert):
    if (meal == "taco"):
        print("1. Cook tortilla")
        print("2. Place cooked chicken onto tortilla.")
        print("3. Add your favorita salsa.")
    else: 
        return("Meal recipe not available.")
    
    if (desert == "ice cream"):
        print("1. Grab a bowl, spoon, your favorite ice cream, and toppings.")
        print("2. Scoop favorite ice cream flavor into bowl.")
        print("3. Add toppings.")
    else: 
        return ("Desert not available.")
    return ("4. Enjoy!")

print(printRecipe("taco", "ice cream"))
