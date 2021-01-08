def max_of_three_numbers(x, y, z):
    if x > y > z:
        return x
    if y > x > z:
        return y
    if z > x > y:
        return z
    if z > y > x:
        return z
    if y > z > x:
        return y
    if x > z > y:
        return x

print(max_of_three_numbers(21,1,4))