def final_amount(p, r, n, t):
    a = p * (1 + (r/n)) ** (n*t)
    return a

toInvest = float(input("How much do you want to invest? "))

fnl = final_amount(toInvest, 0.08, 12, 5)

print("At the end of the period, you will have saved ", fnl, "amount of USD.")
