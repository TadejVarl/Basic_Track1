import turtle  # telling the computer to load a module named turtle.

color = str(input("Background Color:  "))

# definition section
paper = turtle.Screen()
leonardo = turtle.Turtle()

# color section
paper.bgcolor(color)
leonardo.color("red")

# object movement instruction section
leonardo.forward(100)
leonardo.stamp()
leonardo.left(90)
leonardo.forward(100)
leonardo.stamp()
leonardo.forward(30)
leonardo.speed(0.4)
leonardo.right(90)
leonardo.forward(50)
leonardo.stamp()

tess = turtle.Turtle()

tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)

smalling = turtle.Turtle()
smalling.penup()
size = 5

for _ in range(45):
    smalling.stamp()
    size = size + 2
    smalling.shape("turtle")
    smalling.forward(size)
    smalling.right(24)



# exit section (necessary)
paper.exitonclick()
