import sys
sys.path.insert(0, "/home/pi/Documents/Rhoda's Projects/python-turtle/shapes")

from turtle import Turtle, Screen
from time import sleep
from make_circle import draw_circle

turtle = Turtle()
screen = Screen()
screen.colormode(255)

#turtle.color((255,0,0))

side = 25
sideLength = None

for i in range(3):
    for j in range(18):
        if i == 0:
            sideLength = 10
        elif i == 1:
            sideLength = 15
        else:
            sideLength = 20
        draw_circle(side, sideLength, turtle, screen)
        turtle.right(20)
