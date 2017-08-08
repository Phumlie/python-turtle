import turtle
import random

flake = turtle.Screen()
elsa = turtle.Turtle()
flake.bgcolor("white")

colours = ["cyan", "grey", "magenta", "blue"]

elsa.penup()
elsa.forward(90)
elsa.left(45)
elsa.pendown()

def branch():
    for i in range(3):
        for i in range(3):
            elsa.forward(30)
            elsa.backward(30)
            elsa.right(45)
        elsa.left(90)
        elsa.backward(30)
        elsa.left(45)
    elsa.right(90)
    elsa.forward(90)

for i in range(8):
    branch()
    elsa.left(45)

#elsa.color(random.choice(colours))

flake.exitonclick()
