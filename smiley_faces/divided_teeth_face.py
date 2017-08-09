from turtle import Turtle, Screen

turtle = Turtle() 
screen = Screen()
screen.colormode(255)


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
turtle.right(90)
turtle.forward(115)

turtle.backward(19)
turtle.right(90)
turtle.forward(42)
turtle.backward(42)
turtle.right(90)
turtle.forward(19)
turtle.left(90)
turtle.forward(53)
turtle.backward(53)
turtle.right(90)
turtle.forward(19)
turtle.left(90)
turtle.forward(56)
turtle.backward(56)
turtle.right(90)
turtle.forward(19)
turtle.left(90)
turtle.forward(53)
turtle.backward(53)
turtle.right(90)
turtle.forward(19)
turtle.left(90)
turtle.forward(42)

turtle.penup()
turtle.backward(42)
turtle.left(90)
turtle.forward(95)
turtle.pendown()
turtle.right(90)

turtle.right(30)
for i in range(120):
    turtle.forward(1.15)
    turtle.right(1)

turtle.penup()
turtle.forward(200)
