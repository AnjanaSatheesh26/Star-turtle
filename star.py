import turtle

screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.color("yellow")
t.speed(5)

for i in range(5):
    t.forward(100)
    t.right(144)

turtle.done()
