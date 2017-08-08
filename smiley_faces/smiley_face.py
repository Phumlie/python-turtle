from turtle import Turtle, Screen

turtle = Turtle() 
screen = Screen()


side = 80
angle = 360/side
sideLength = 10

for i in range(side):
    turtle.forward(sideLength)
    turtle.right(angle)

turtle.penup()
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.pendown()
for i in range(side):
    turtle.forward(1)
    turtle.right(angle)
turtle.penup()
turtle.backward(100)
turtle.pendown()
for i in range(side):
    turtle.forward(1)
    turtle.right(angle)

turtle.penup()
turtle.left(90)
turtle.forward(90)
turtle.left(90)
turtle.forward(15)
turtle.right(90)
turtle.pendown()
for i in range(180):
    turtle.forward(1)
    turtle.right(1)
