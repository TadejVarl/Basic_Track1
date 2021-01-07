# this is Vincent's way
n = 25
threshold = 1e-8
approximation = n / 2

while True:
    better = (approximation + n / approximation) / 2
    if abs(approximation - better) < threshold:
        break
    print("better\t", better)
    approximation = better

print("best\t", better)