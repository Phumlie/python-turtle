from turtle import Turtle, Screen
from time import sleep

turtle = Turtle()
screen = Screen()
screen.colormode(255)

R = 255
G = 0
B = 0

R2 = 159
G2 = 100
B2 = 0

R3 = 105
G3 = 0
B3 = 145

R4 = 50
G4 = 0
B4 = 0

side = 100
angle = 90


sleep(0.5)

turtle.color((R, G, B))
turtle.forward(side)
turtle.backward(side)
turtle.right(angle)
turtle.color((R2, G2, B2))
turtle.forward(side)
turtle.backward(side)
turtle.right(angle)
turtle.color((R3, G3, B3))
turtle.forward(side)
turtle.backward(side)
turtle.right(angle)
turtle.color((R4, G4, B4))
turtle.forward(side)
turtle.backward(side)
turtle.right(angle)
