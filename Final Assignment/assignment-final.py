"""Python Track"""

__author__ = "Tadej Varl"

import csv

with open('nutritional_values.csv', 'w', newline='') as file_name:
    writer = csv.DictWriter(file_name, fieldnames=["Ingredient", "Unit", "Calories", "Fat", "Carbs", "Protein"])
    writer.writeheader()


def get_recipe_ingredients():
    ingredient_list = []

    while True:
        ingredient = input("Provide the name of an ingredient included in the recipe (q to quit): ")
        if str.lower(ingredient) == "q":
            if not ingredient_list:
                str(print("You cannot prepare any food with no ingredients. Add some!"))
            break
        if str(ingredient) != "q":
            ingredient_list.append(ingredient)

    if len(ingredient_list) >= 1:
        print("Your recipe includes the following ingredients:", ingredient_list, ". SOUNDS DELICIOUS!")

    return ingredient_list


def get_nutritional_values(ingredient_list) -> dict:
    global unit
    nutritional_value_dict = {}  # This is an empty dictionary which will contain nutritional value for each of
    # the ingr.

    for ingredient in ingredient_list:
        if ingredient not in nutritional_value_dict:
            unit = int(
                input("Please provide the value for unit (in grams or mL) of the ingredient " + ingredient + ". "))
            calories = float(input("Please provide the value for calories of the ingredient " + ingredient + ". "))
            fat = float(input("Please provide the value for fat of the ingredient " + ingredient + ". "))
            carbohydrate = float(
                input("Please provide the value for carbohydrate of the ingredient " + ingredient + ". "))
            protein = float(input("Please provide the value for protein of the ingredient " + ingredient + ". "))
        nutritional_value_dict[ingredient] = unit, calories, fat, carbohydrate, protein

    print(nutritional_value_dict)

    with open("nutritional_values.csv", "a") as file_name:
        for ingredient in nutritional_value_dict:
            file_name.write("%s,%s\n" % (ingredient, nutritional_value_dict[ingredient]))

        return nutritional_value_dict


def get_amounts(ingredient_list, nutritional_value_dict: dict) -> dict:
    """
    Given a list of ingredients and a dictionary of nutritional values
    ask the user to provide how much of each ingredient should be used in the recipe
    """
    amounts = {}  # amounts is a new list used for storing exact portions

    with open("nutritional_values.csv", "r"):
        for ingredient in ingredient_list:
            unit, calories, fat, carbohydrate, protein = nutritional_value_dict[ingredient]
            multiplier = int(input("How many times of a given g or mL of " + ingredient + " "
                                                                                          "you be using in a recipe? "))

            amounts[ingredient] = [(unit * multiplier), (calories * multiplier), (fat * multiplier),
                                   (carbohydrate * multiplier), (protein * multiplier)]

        print(amounts)

    with open("nutritional_values.csv", "w") as file_name:
        for ingredient in amounts:
            file_name.write("%s,%s\n" % (ingredient, amounts[ingredient]))

    return amounts


def generate_table(amounts_list: dict):
    """
    ask the user for a quantity per ingredient
    generate a table with nutrient information per ingredient and a total for the recipe
    also generate a line of the total per portion (ask the user for the number of portions)
    """

    amounts_list

    with open('nutritional_values.csv', 'w', newline='') as file_name:
        writer = csv.DictWriter(file_name, fieldnames=["Ingredient", "Unit", "Calories", "Fat", "Carbs", "Protein"])
        writer.writeheader()

    with open('nutritional_values.csv', 'r') as file_name:
        reader = csv.reader(file_name)
        next(reader, None)
        new_dict = {}

        for row in reader:
            new_dict[row[0]] = [row[1], row[2], row[3], row[4], row[5]]
        print(new_dict)

    print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format('ITEM', 'UNIT', 'CALORIES', 'FAT', 'CARBS', 'PROTEIN'))

    for key, value in amounts_list.items():
        item = key
        unit, kCal, fat, carbs, protein = value
        print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} ".format(item, unit, kCal, fat, carbs, protein))


if __name__ == '__main__':
    # 1.  Ask for a list of ingredients.
    ingredients = get_recipe_ingredients()
    # 2. Get nutrient information for each of these ingredients.
    nutritional_values = get_nutritional_values(ingredients)

    amounts_list = get_amounts(ingredients, nutritional_values)

    generate_table(amounts_list)
