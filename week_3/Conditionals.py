# CONDITIONAL STATEMENTS

number = int(input(" What is x? "))

leftover = number % 2

if leftover == 0:
    print(number, " is even.")
    print("Did you know that 2 is the only even prime number?")
else:
    print(number, " is odd.")
    print("Did you know that multiplying two odd numbers always given an odd result?")