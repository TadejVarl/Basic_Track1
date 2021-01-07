side_1 = 15
side_2 = 20
hypotenuse = 25
threshold = 1e-7


sum_squares = (side_1 **2) + (side_2**2)
hypotenuse_square = hypotenuse**2

if abs(sum_squares - hypotenuse_square) < threshold:
    print("This is a right angled triangle")

else:
    print("This is not a right angled triangle")