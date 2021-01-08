# THIS IS A FUNCTIONS EXERCISE

# WE BEGIN WITH SUMMING UP TWO NUMBERS THAT USER WILL PROVIDE WHEN CALLING A FUNCTION
def sum_of_two_numbers(a, b):
    return(a+b)                     # return is what we use this time

# You have to use a print function in order to view the result of the sum
print(sum_of_two_numbers(9,1))


def sum_of_a_list(numbers):
    total = 0                       # we should always define a starting point of the sum, which is 0 in this case
    for x in numbers:               # inside a function, make a for loop
        total += x                  # made a mistake and tried to write numbers instead of x
    return total                    # we also use return here

print(sum_of_a_list((3,5,11,1,1)))