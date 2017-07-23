from turtle import Turtle, Screen
from time import sleep

turtle = Turtle()
screen = Screen()
screen.colormode(255)

turtle.color((200,0,100))

sleep = 0.5


for i in range(24):
    if i == 8:
        turtle.right(60)
    elif i == 16:
        turtle.right(80)
    for k in range(8):
        turtle.forward(50)
        turtle.right(45)
    turtle.left(45)
    
        
    
        
