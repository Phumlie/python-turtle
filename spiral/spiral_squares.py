from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
screen.colormode(255)

odd = True

length = 100;
diff = 10

for i in range(30):
  if odd == True:
      turtle.color((255,0,0))
      odd = False
  else:
      turtle.color((0,0,255))
      odd = True
  for j in range(4):
      turtle.forward(length)
      turtle.right(90)
  length = length - diff
  if length < diff:
      length = diff
  turtle.right(25)
