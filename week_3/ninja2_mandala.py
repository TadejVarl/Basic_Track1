import turtle

paper = turtle.Screen()
leonardo = turtle.Turtle()              # first turtle
leonardo.shape("turtle")                # nastavitev oblike
leonardo.speed(10)                      # nastavitev barve

for number in [0, 1, 2, 3, 4, 5]:
    leonardo.forward(50)
    leonardo.left(60)
    print(number)


davinci = turtle.Turtle()
davinci.shape("circle")
davinci.speed(20)

for element in range(10):               # second turtle
    davinci.forward(90)
    davinci.left(36)
    print(element)

colors = ["yellow", "red", "purple", "blue"]
for color in colors:                    # third turtle
    davinci.color(color)
    davinci.forward(50)
    davinci.left(90)


paper.exitonclick()