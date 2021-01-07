set = [421, 986, -422, 999, -1, 2, 6, 444, -1995, 765, 890, -9000]

negative_numbers = 0
for numbers in set:
    if numbers < 0:
        negative_numbers += numbers


print("The sum of negative numbers is:", negative_numbers)