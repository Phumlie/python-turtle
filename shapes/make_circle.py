from turtle import Turtle, Screen
from time import sleep

def draw_circle(side, sideLength, turtle, screen):
        
    sleep(0.5)
    angle = 360/side

    colorSelect = 1

    for i in range(side):
        if colorSelect == 1:
            turtle.color((255,0,0))
            colorSelect = 2
        elif colorSelect == 2:
            turtle.color((0,100,0))
            colorSelect = 3
        elif colorSelect == 3:
            turtle.color((0,0,255))
            colorSelect = 1   
        turtle.forward(sideLength)
        turtle.right(angle)
