numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_even = 0
for number in numbers:
    if number % 2 == 0:
        break
    else:
        sum_even += number

print("Sum of the elements up to but not including the first even number is:", sum_even)