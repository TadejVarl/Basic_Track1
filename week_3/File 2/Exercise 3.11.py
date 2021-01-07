import turtle  # telling the computer to load a module named turtle.

# definition section
paper = turtle.Screen()
clock = turtle.Turtle()

# color setting
paper.bgcolor("green")
clock.color("navyblue")
clock.shape("turtle")

for i in range(12):
    clock.penup()
    clock.forward(200)
    clock.stamp()
    clock.back(200)
    clock.stamp()
    clock.left(30)

paper.exitonclick()