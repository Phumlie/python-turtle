from turtle import Turtle, Screen
from time import sleep

turtle = Turtle()
screen = Screen()
screen.colormode(255)

turtle.color((200,0,100))

sleep = 0.5


for i in range(9):
    for k in range(5):
        turtle.right(72)
        turtle.forward(100)
    turtle.left(40)
