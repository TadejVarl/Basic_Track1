set = [421, 986, 422, 999, 1, 2, 6, 444, 1995, 765, 890, 9000]

even_numbers = 0
for numbers in set:
    if numbers % 2 == 0:
        even_numbers += numbers

print("The sum of even numbers is:", even_numbers)