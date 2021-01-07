import turtle

paper = turtle.Screen()
leonardo = turtle.Turtle()

paper.bgcolor("lightgreen")
leonardo.color("pink")
leonardo.pensize(6)

leonardo.penup()
leonardo.goto(-600,0)
leonardo.pendown()

for i in range(4):
    leonardo.forward(90)
    leonardo.left(90)

leonardo.penup()
leonardo.forward(180)
leonardo.pendown()

for i in range(4):
    leonardo.forward(90)
    leonardo.left(90)

leonardo.penup()
leonardo.forward(180)
leonardo.pendown()

for i in range(4):
    leonardo.forward(90)
    leonardo.left(90)

leonardo.penup()
leonardo.forward(180)
leonardo.pendown()

for i in range(4):
    leonardo.forward(90)
    leonardo.left(90)

leonardo.penup()
leonardo.forward(180)
leonardo.pendown()

for i in range(4):
    leonardo.forward(90)
    leonardo.left(90)

leonardo.penup()
leonardo.forward(180)
leonardo.pendown()
leonardo.stamp()


paper.exitonclick()
