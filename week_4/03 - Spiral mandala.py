import turtle


window = turtle.Screen()
window.bgcolor("white")

leonardo = turtle.Turtle()

colors = ["red", "blue", "purple", "yellow" ]

for i in range(360):
    leonardo.pencolor(colors[i%4])
    leonardo.width(i/ 250 + 1)
    leonardo.forward(i)
    leonardo.left(59)







window.exitonclick()
