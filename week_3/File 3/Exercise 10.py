import turtle

way = [(160, 20), (-43, 10), (270, 8), (-43, 12)]

screen = turtle.Screen()
drunk_pirate = turtle.Turtle()

for (angle, steps) in way:
    drunk_pirate.left(angle)
    drunk_pirate.forward(steps)

screen.exitonclick()