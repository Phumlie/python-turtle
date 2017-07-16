from turtle import Turtle, Screen
from time import sleep

turtle = Turtle()
screen = Screen()

sleep(0.5)

for number in range(2):
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
