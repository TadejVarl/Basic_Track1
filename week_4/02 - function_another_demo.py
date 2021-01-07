import turtle

# set up the window and its attributes

window = turtle.Screen()
window.bgcolor("purple")
window.title("FLAG OF SLOVENIA!")


def draw_shape(name, size, pensize):

    # make animal draw a square with sides of lenght size

    for color in("red", "blue", "white", "yellow"):
        name.color(color)
        name.forward(size)
        name.left(90)
        name.pensize(pensize)

tadej = turtle.Turtle()

size = 20
for i in range(20):
    draw_shape(tadej, size, 9)
    size += 10
    tadej.forward(10)
    tadej.right(18)

turtle.speed(10)

window.exitonclick()
