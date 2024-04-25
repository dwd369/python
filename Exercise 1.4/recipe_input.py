import pickle

# function to calculate recipe difficulty
def calc_difficulty(cooking_time, num_ingredients):
    if cooking_time < 10 and num_ingredients < 4:
        return "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        return "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        return "Intermediate"
    else:
        return "Hard"

# function to allow user creating a recipe
def take_recipe(recipe_num):
    print(f"\n---- Recipe #{recipe_num} ----")

    # Validate recipe name
    while True:
        name = input("Enter your recipe name: ").strip()
        if name:
            break
        print("\nPlease enter a valid recipe name.")

    # Validate cooking time
    while True:
        try:
            cooking_time = int(input("Enter the cooking time (in minutes): "))
            if cooking_time > 0:
                break
            print("\nPlease enter a positive number for the cooking time.")
        except ValueError:
            print("\nInvalid input! Please enter a number.")

    # Validate ingredients
    while True:
        ingredients_input = input("Enter your ingredients, seperated by a comma: ").strip()
        ingredients = [ingredient.strip() for ingredient in ingredients_input.split(",") if ingredient.strip()]
        if ingredients:
            break
        print("\nPlease enter at least one ingredient.")
    
    difficulty = calc_difficulty(cooking_time, len(ingredients))
    return {"name": name, "cooking_time": cooking_time, "ingredients": ingredients, "difficulty": difficulty}

# prompt user for enter the recipe filename
filename = input("Enter the filename to save the recipes: ")

# error handling if no file was found based on the user entered name
try:
    with open(filename, "rb") as file:
        data = pickle.load(file)
except FileNotFoundError:
    data = {"recipes_list": [], "all_ingredients": []}
except Exception as e:
    print(f"An error occured: {e}")
    data = {"recipes_list": [], "all_ingredients": []}

recipes_list, all_ingredients = data["recipes_list"], data["all_ingredients"]

# prompt user to enter the number of recipe they would like to add
n = int(input("\nHow many recipes would you like to enter?: "))
for i in range(1, n+1):
    recipe = take_recipe(i)
    recipes_list.append(recipe)
    for ingredient in recipe["ingredients"]:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)

# write recipe data into user's defined filename
data = {"recipes_list": recipes_list, "all_ingredients": all_ingredients}
    
with open(filename, "wb") as file:
    pickle.dump(data, file)

print("\nRecipes saved successfully!")