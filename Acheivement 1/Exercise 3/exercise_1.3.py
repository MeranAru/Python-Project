recipe_list = []

ingredients_list = []

def take_recipe():
    name = input("name of recipe: ")
    cooking_time = int(input("cooking_time(min): "))
    ingredients = input("ingredients for the recipe: ").split(", ")

    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients
    }
    return recipe

n = int(input("how many recipes would you like to make?"))

for i in range(n):

    recipe = take_recipe()
    for ingredient in recipe["ingredients"]:
        if not ingredient in ingredients_list:
            ingredients_list.append(ingredient)
        recipe_list.append(recipe)

for recipe in recipe_list:
    #cooking_time is less than 10 minutes, and the number of ingredients is less than 4, set a variable called difficulty to the value of Easy
    if recipe["cooking_time"] < 10 and len(recipe["ingredients"]) <= 4:
        recipe["difficulty"] = "easy"
    elif recipe["cooking_time"] < 10 and len(recipe["ingredients"]) <=4:
        recipe["difficulty"] = "medium"
    elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) <4:
        recipe["difficulty"] = "intermediate"
    elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) >=4:
        recipe["difficulty"] = "hard"

    print("recipe: ", recipe["name"])
    print("cooking_time(min): ", recipe["cooking_time"])
    print("ingredients: ", recipe["ingredients"])
    print("difficulty: ", recipe["difficulty"])

    def print_ingredients():
        ingredients_list.sort()
        print("ingredients available for all recipes")
        for ingredient in ingredients_list:
            print(ingredient)

    print_ingredients()