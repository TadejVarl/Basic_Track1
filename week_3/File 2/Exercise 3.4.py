numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# a
for x in numbers:
    print("This is a new line with a new number: ", x)
# b
for x in numbers:
    print("This is a new line with a new number: ", x, ", and a square of that number: ",  x * x)

# c
total = 0
for x in numbers:
    total += x
    print("The sum of the numbers is:", total)

# d
product = 1
for x in numbers:
    product *= x
    print("The product of the numbers is: ", product)