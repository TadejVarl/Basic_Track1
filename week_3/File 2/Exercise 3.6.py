import turtle  # telling the computer to load a module named turtle.

color = str(input("Background Color:  "))

# definition section
paper = turtle.Screen()
drunk_pirate = turtle.Turtle()

paper.bgcolor(color)

angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]

for angle in angles:
    drunk_pirate.forward(100)
    drunk_pirate.left(angle)



