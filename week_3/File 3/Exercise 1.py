set = [421, 986, 422, 999, 1, 2, 6, 444, 1995, 765, 890, 9000]

count_uneven = 0
for number in set:
    if number % 2 != 0:
        count_uneven += 1


print("There were", count_uneven, "uneven numbers in the list")