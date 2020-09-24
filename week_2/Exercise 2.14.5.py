# first define the variables


r = 1 / 100  # realistic nominal interest rate
n = 3  # yearly compounding frequency
t = 10  # number of years
P = int(
    input("You're opening a savings account for the duration of 10 years. What is your principal amount in dollars: "))

A = P * (1 + r / n) ** (n * t)

print("Your savings at the end of year ", t, " will amount for: ", A)
