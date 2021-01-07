import turtle  # telling the computer to load a module named turtle.

color = str(input("Background Color:  "))

# definition section
paper = turtle.Screen()
triangle = turtle.Turtle()

paper.bgcolor(color)

for i in range(3):
    triangle.forward(80)
    triangle.left(120)


square = turtle.Turtle()            # define new object

for i in range(4):
    square.forward(180)
    square.left(90)

hexagon = turtle.Turtle()           # define new object

for i in range(6):
    hexagon.pensize(3)
    hexagon.forward(80)
    hexagon.left(60)

octagon = turtle.Turtle()           # define new object

for i in range(8):
    octagon.pensize(6)
    octagon.forward(90)
    octagon.left(45)