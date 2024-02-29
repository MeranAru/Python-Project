class Recipe(object):
    all_ingredients = []

    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.cooking_time = 0
        self.difficulty = None

    
    def get_name(self):
        output = "Recipe name: " + str(self.name)
        return output
    
    def set_name(self, name):
        self.name = str(name)

    def get_cooking_time(self):
        output = "Cooking time: " + str(self.cooking_time)
        return output
    
    def set_cooking_time(self, cooking_time):
        self.cooking_time = int(cooking_time)

    def add_ingredients(self, *ingredients):
        self.ingredients = list(ingredients)
        self.update_all_ingredients()

    def get_ingredients(self):
        return self.ingredients
    
    def calculate_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients) < 4:
            return 'Easy'
        elif self.cooking_time < 10 and len(self.ingredients) >= 4:
            return 'Medium'
        elif self.cooking_time >= 10 and len(self.ingredients) < 4:
            return 'Intermediate'
        elif self.cooking_time >= 10 and len(self.ingredients) >= 4:
            return 'Hard'
        
    def get_difficulty(self):
        if self.difficulty is None:
            self.difficulty = self.calculate_difficulty()
        return self.difficulty

    def search_ingredient(self, ingredient, ingredients):
        if ingredient in self.ingredients:
            return True
        else:
            return False
        
    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in self.all_ingredients:
                self.all_ingredients.append(ingredient)

    def __str__(self):
        output = '\nRecipe Name: ' + str(self.name) + \
            '\nCooking time in minutes: ' + str(self.cooking_time) + \
            '\nDifficulty: ' + str(self.difficulty) + \
            '\nIngredients:' + \
            '\n------------ \n'
        for ingredient in self.ingredients:
            output += '- ' + ingredient + '\n'
        return output
    
    def recipe_search(recipes_list, ingredient):
        for recipe in recipes_list:
            if recipe.search_ingredient(ingredient, recipe.ingredients):
                print(recipe)

    def view_recipe(self):
        print('\nName: ' + str(self.name))
        print('\nCooking time: ' + str(self.cooking_time))
        print('\nDifficulty: ' + str(self.difficulty))
        print('\nIngredients: ')
        show_ingredients = self.get_ingredients()
        for ingredient in show_ingredients:
            print(ingredient)

recipes_list = []

tea = Recipe("Tea")
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
tea.set_cooking_time(5)
tea.get_difficulty()

recipes_list.append(tea)

coffee = Recipe("Coffee")
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
coffee.set_cooking_time(5)
coffee.get_difficulty()

recipes_list.append(coffee)

cake = Recipe("Cake")
cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk" )
cake.set_cooking_time(50)
cake.get_difficulty()

recipes_list.append(cake)

banana_smoothie = Recipe("Banana Smoothie")
banana_smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
banana_smoothie.set_cooking_time(5)
banana_smoothie.get_difficulty()

recipes_list.append(banana_smoothie)

print("Recipe Lists: ")
print("(-----------------------------------")

for recipe in recipes_list:
    print(recipe)

print("Results for all recipes with Water: " )
print("-----------------------------------" )
Recipe.recipe_search(recipes_list, "Water")

print("Results for all recipes with Sugar: " )
print("-----------------------------------" )
Recipe.recipe_search(recipes_list, "Sugar")

print("Results for all recipes with Bananas: " )
print("-----------------------------------" )
Recipe.recipe_search(recipes_list, "Bananas")