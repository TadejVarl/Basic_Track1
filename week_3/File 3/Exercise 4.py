countries = ["Chile", "Slovenia", "Denmark", "Syria", "Greece", "China", "USA"]

length_5 = 0
for country in countries:
    if len(country) == 5:
        length_5 += 1

print("There are", length_5, "countries with the name lenght of 5.")