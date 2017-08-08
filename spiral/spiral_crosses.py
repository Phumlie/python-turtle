from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
screen.colormode(255)

turtle.color((255,0,0))


for i in range(31):
    for i in range(4):
        turtle.right(90)
        turtle.forward(100)
        turtle.backward(100)
    turtle.left(70)
    turtle.forward(100)
