from turtle import Turtle, Screen
from time import sleep

turtle = Turtle()
screen = Screen()

sleep(0.5)
side = 100

for number in range(3):
    if number == 0:
        turtle.right(60)
        turtle.forward(side)
    else:
        turtle.right(120)
        turtle.forward(side)
        
