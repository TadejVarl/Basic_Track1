import turtle


def draw_square(animal, size):
    """
    Draw a square
    """

    for _ in range(6):
        animal.forward(size)
        animal.left(60)


screen = turtle.Screen()
nick = turtle.Turtle()

for _ in range(4):
    draw_square(nick, 100)
    nick.left(6)



screen.exitonclick()