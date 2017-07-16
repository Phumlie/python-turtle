from turtle import Turtle, Screen
from time import sleep

turtle = Turtle()
screen = Screen()

sleep(0.5)
side = 100
angle = 90

for number in [1,2,3,4]:
    turtle.forward(side)
    turtle.backward(side)
    turtle.right(angle)
