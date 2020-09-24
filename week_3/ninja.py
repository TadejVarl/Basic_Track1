import turtle

paper = turtle.Screen()
leonardo = turtle.Turtle()

leonardo.forward(50)
leonardo.stamp()
leonardo.penup()
leonardo.forward(20)
leonardo.pendown()
leonardo.stamp()
leonardo.forward(30)
leonardo.speed(0.4)
leonardo.right(90)
leonardo.forward(50)
leonardo.stamp()

paper.exitonclick()