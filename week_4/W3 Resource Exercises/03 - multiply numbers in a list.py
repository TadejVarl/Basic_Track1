def multiply_list(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total


print(multiply_list((-1,2,3,4)))