"""Provide an overview of the nutritional values of a recipe"""

__author__ = "Nadine Hebendanz"

import os

from typing import List

Strings = List[str]


def get_recipe_ingredients() -> Strings:
    """
    Asks the user for a list of ingredients that will be included in a recipe
    """
    input_string = input("Enter ingredients separated by space ")
    ingredient_list = input_string.strip().lower().split(" ")

    # print("Printing all ingredients")
    # for name in ingredient_list:
    #     print(name)

    return ingredient_list


def get_nutritional_values(ingredient_list: Strings, file_name="nutritional_values.csv") -> dict:
    """
    Tries to get nutritional values for each of the ingredients in the list from a file
    Asks the user for the nutritional values if not yet available in the file and writes them to the file for future use
    """
    nutritional_value_dict = {}

    if not os.path.isfile(file_name):
        with open(file_name, "w") as nutritional_value_file:
            nutritional_value_file.write("name,unit,kcal,fat,carbohydrate,protein")

    with open(file_name, "r") as nutritional_value_file:
        for line in nutritional_value_file:
            name, unit, kcal, fat, carbohydrate, protein = line.split(",")
            nutritional_value_dict[name] = (unit, kcal, fat, carbohydrate, protein)

    for ingredient in ingredient_list:
        if ingredient not in nutritional_value_dict:
            print('Please provide the nutritional values for ' + ingredient + ':')
            unit = str(input("\tGive the value for unit "))
            kcal = str(input("\tGive the value for kcalories "))
            fat = str(input("\tGive the value for fat "))
            carbohydrate = str(input("\tGive the value for carbohydrate "))
            protein = str(input("\tGive the value for protein "))
            nutritional_value_dict[ingredient] = (unit, kcal, fat, carbohydrate, protein)

    with open(file_name, 'w') as file:
        for name in nutritional_value_dict:
            unit, kcal, fat, carbohydrate, protein = nutritional_value_dict[name]
            file.write(name + "," + str(unit) + "," + str(kcal) + "," + str(fat) + "," + str(carbohydrate) + "," + str(protein).rstrip() + "\n")

    return nutritional_value_dict


def get_nutritional_value(ingredient: str, nutrient_list: Strings) -> dict:
    """
    Given a list of nutrients and the name of an ingredient,
    asks the user to provide this information.
    """
    values = {}
    unit, kcal, fat, carbohydrate, protein = nutrient_list[ingredient]
    values = (unit, float(kcal), float(fat), float(carbohydrate), float(protein))

    return values


def get_amounts(ingredient_list: Strings, nutritional_value_dict: dict) -> dict:
    """
    Given a list of ingredients and a dictionary of nutritional values
    ask the user to provide how much of each ingredient should be used in the recipe
    """
    amounts = {}
    amounts['total'] = ('Total', '\t', 0, 0, 0, 0)

    for ingredient in ingredient_list:
        nutritional_values = get_nutritional_value(ingredient, nutritional_value_dict)

        amount = float(input("How much " + nutritional_values[0] + " of " + ingredient + ": "))
        amounts[ingredient] = (
            ingredient,
            amount,
            nutritional_values[1] * amount,
            nutritional_values[2] * amount,
            nutritional_values[3] * amount,
            nutritional_values[4] * amount
        )

        amounts['total'] = (
            amounts['total'][0],
            amounts['total'][1],
            amounts['total'][2] + amounts[ingredient][2],
            amounts['total'][3] + amounts[ingredient][3],
            amounts['total'][4] + amounts[ingredient][4],
            amounts['total'][5] + amounts[ingredient][5]
        )

    return amounts


def generate_table(amounts: dict, nutritional_value_dict: dict):
    """
    ask the user for a quantity per ingredient
    generate a table with nutrient information per ingredient and a total for the recipe
    also generate a line of the total per portion (ask the user for the number of portions)
    """
    table_string = "Name \t \t \t kcalories \t fat \t carbohydrate \t protein"

    for ingredient in amounts:
        if ingredient == 'total':
            table_string += "\n" + str(amounts[ingredient][0])
            table_string += "\t" + str(amounts[ingredient][1])
            table_string += "\t" + str(amounts[ingredient][2])
            table_string += "\t" + str(amounts[ingredient][3])
            table_string += "\t" + str(amounts[ingredient][4])
            table_string += "\t" + str(amounts[ingredient][5])
        else:
            table_string += "\n" + str(ingredient)
            table_string += "\t" + str(amounts[ingredient][1])
            table_string += "\t" + str(nutritional_value_dict[ingredient][0])
            table_string += "\t" + str(nutritional_value_dict[ingredient][1])
            table_string += "\t" + str(nutritional_value_dict[ingredient][2])
            table_string += "\t" + str(nutritional_value_dict[ingredient][3])
            table_string += "\t" + str(nutritional_value_dict[ingredient][4].rstrip())

    # print(table_string)
    with open('output.txt', 'w') as file:
        file.write(table_string)



    ## html output
    table_string = "<html><body><table>" \
                   "<tr>" \
                   "<td>Name</td>" \
                   "<td>&nbsp;</td>" \
                   "<td>&nbsp;</td>" \
                   "<td>kcalories</td>" \
                   "<td>fat</td>" \
                   "<td>carbohydrate</td>" \
                   "<td>protein</td>" \
                   "</tr>"

    for ingredient in amounts:
        if ingredient == 'total':
            table_string += "<tr><td>" + str(amounts[ingredient][0]) + "</td>"
            table_string += "<td>&nbsp;</td><td>&nbsp;</td>"
            table_string += "<td>" + str(amounts[ingredient][2]) + "</td>"
            table_string += "<td>" + str(amounts[ingredient][3]) + "</td>"
            table_string += "<td>" + str(amounts[ingredient][4]) + "</td>"
            table_string += "<td>" + str(amounts[ingredient][5]) + "</td>"
            table_string += "</tr>"
        else:
            table_string += "<tr><td>" + str(ingredient) + "</td>"
            table_string += "<td>" + str(amounts[ingredient][1]) + "</td>"
            table_string += "<td>" + str(nutritional_value_dict[ingredient][0]) + "</td>"
            table_string += "<td>" + str(nutritional_value_dict[ingredient][1]) + "</td>"
            table_string += "<td>" + str(nutritional_value_dict[ingredient][2]) + "</td>"
            table_string += "<td>" + str(nutritional_value_dict[ingredient][3]) + "</td>"
            table_string += "<td>" + str(nutritional_value_dict[ingredient][4].rstrip()) + "</td>"
            table_string += "</tr>"

    table_string += "</table></body></html>"

    with open('output.html', 'w') as file:
        file.write(table_string)


if __name__ == '__main__':
    # 1.  Ask for a list of ingredients.
    ingredients = get_recipe_ingredients()

    # 2. Get nutrient information for each of these ingredients.
    nutritional_values = get_nutritional_values(ingredients)

    # 3. Ask for a list of amounts for each of the ingredients.
    amounts_list = get_amounts(ingredients, nutritional_values)

    # 4. Based on the information retrieved generate a meaningful output.
    generate_table(amounts_list, nutritional_values)
