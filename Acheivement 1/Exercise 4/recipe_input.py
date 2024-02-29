import pickle

def take_recipe():
    name = input("name of recipe: ")
    cooking_time = int(input("cooking_time(min): "))
    ingredients = input("ingredients for the recipe: ").split(", ")

    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients
    }

    recipe["difficulty"] = calc_difficulty(recipe)
    return recipe

def calc_difficulty(recipe):
    #cooking_time is less than 10 minutes, and the number of ingredients is less than 4, set a variable called difficulty to the value of Easy
    if recipe["cooking_time"] < 10 and len(recipe["ingredients"]) <= 4:
        recipe["difficulty"] = "easy"
    elif recipe["cooking_time"] < 10 and len(recipe["ingredients"]) >= 4:
        recipe["difficulty"] = "medium"
    elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) < 4:
        recipe["difficulty"] = "intermediate"
    elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) >= 4:
        recipe["difficulty"] = "hard"

all_ingredients = []
recipes_list = []

filename = input("please enter a filename with your recipes -") + ".bin"
data = { "recipes_list":[], "all_ingredients":[] } 

try:
    recipes_file = open(filename, "rb")
    data = pickle.load(recipes_file)
    
except FileNotFoundError:
    print("file not found. creating new file")   
    
except:
    print("unexpected error. creating new file")
    
else:
    recipes_file.close()

finally:
    recipes_list = data["recipes_list"]
    all_ingredients = data["all_ingredients"]    
    
    
    num = int(input("how many recipes would you like to create? -"))
    
    for i in range(num):
        recipe = take_recipe()
        for ingredient in recipe["ingredients"]:
            if not ingredient in all_ingredients:
                all_ingredients.append(ingredient)
        recipes_list.append(recipe)
        
data = {
    "recipes_list": recipes_list,
    "all_ingredients": all_ingredients
}

recipes_file = open(filename, "wb")
pickle.dump(data, recipes_file)
print("your file has been updated.")
