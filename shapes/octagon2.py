from turtle import Turtle, Screen
from time import sleep

turtle = Turtle()
screen = Screen()

sleep(0.5)
side = 8
angle = 360/side
sideLength = 100

for number in range(side):
    turtle.forward(sideLength)
    turtle.right(angle)
