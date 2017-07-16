from turtle import Turtle, Screen
from time import sleep

def draw_circle(side, sideLength):
    turtle = Turtle()
    screen = Screen()

    sleep(0.5)
    angle = 360/side

    for number in range(side):
        turtle.forward(sideLength)
        turtle.right(angle)

draw_circle(30, 15)
