from turtle import Turtle, Screen
from time import sleep

turtle = Turtle()
screen = Screen()
screen.colormode(255)

turtle.color((155,0,55))

sleep = 0.5
sideLength = 100


for i in range(24):
    for i in range(3):
        if i == 0:
            turtle.right(60)
            turtle.forward(sideLength)
        else:
            turtle.right(120)
            turtle.forward(sideLength)
           
    turtle.left(45)
