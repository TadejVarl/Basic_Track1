import csv

csv_columns = ['Item','Unit','Calories','Fat','Carbs','Protein']

ingredients_list = {}

program_run = True

while program_run:
        item = input("Choose an ingredient or [q] to quit: ")
        if str.lower(item) == "q":
                break
        else:
            if item in ingredients_list:
                print("Item already on the list!")
                break
            else:
                unit = int(input("How much of an ingredient will you be needing [g]: "))
                kCal = int(input("How many calories does this ingredient has: "))
                fat = int(input("How many fat does this ingredient has: "))
                carbs = int(input("How many carbs does this ingredient has: "))
                protein = int(input("How many protein does this ingredient has: "))

        ingredients_list[item] = unit, kCal, fat, carbs, protein

csv_file = "nutritional_values.csv"
csv_columns = ['Item','Unit','Calories','Fat','Carbs','Protein']

if len(ingredients_list) == 0:
    print("You have not chosen any items: ")
else:
    try:
        with open("nutritional_values.csv", 'a') as csvfile:
            w = csv.DictWriter(csvfile, fieldnames=csv_columns)
            if csvfile.tell() == 0:
                w.writeheader()
            for key in ingredients_list.keys():
                csvfile.write("%s,%s\n" % (key, str(ingredients_list[key])[1:-1]))
    except IOError:
        print("I/O error")

with open('nutritional_values.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    next(reader, None)
    new_dict = {}

    for row in reader:
        new_dict[row[0]] = [row[1], row[2], row[3], row[4], row[5]]
    print(new_dict)

print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format('ITEM', 'UNIT', 'CALORIES', 'FAT', 'CARBS', 'PROTEIN'))

for key, value in new_dict.items():
    item = key
    unit, kCal, fat, carbs, protein = value
    print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} ".format(item, unit, kCal, fat, carbs, protein))