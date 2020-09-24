import turtle

paper = turtle.Screen()
leonardo = turtle.Turtle()

for element in [0, 1, 2, 3, 4, 5]:
    leonardo.forward(50)
    leonardo.left(60)
    print(element)


paper.exitonclick()