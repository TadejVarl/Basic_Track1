import turtle  # telling the computer to load a module named turtle.

color = str(input("Background Color:  "))

# definition section
paper = turtle.Screen()
star = turtle.Turtle()

paper.bgcolor(color)

for i in range(5):
    star.forward(50)
    star.left(144)