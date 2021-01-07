import turtle


# bakcground picture
window = turtle.Screen()
turtle.bgpic("random.gif")

def draw_polygon(drawing_turtle: turtle.Turtle, sides = 4, size = 50):       #specifiyng default values for instance sides = 4, size = 25

    for side in range(sides):
        drawing_turtle.forward(size)
        drawing_turtle.left(360 / sides)




edita = turtle.Turtle()
screen = turtle.Screen()

draw_polygon(edita, 8, 20)
draw_polygon(edita)

for no_sides in range(3, 12):
    draw_polygon(edita, no_sides, 10 * no_sides)

screen.exitonclick()