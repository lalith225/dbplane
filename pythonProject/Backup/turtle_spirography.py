import turtle
from turtle import Turtle,Screen
import random

turtle.colormode(255)
turtle.pensize(1)
turtle.speed(0)

def generate_color():
    r = random.randint(1,255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    random_color = (r,g,b)
    return random_color

for i in range(10,100):
    turtle.circle(100)
    turtle.forward(2)
    turtle.right(5)
    turtle.pencolor(generate_color())

my_screen = Screen()
my_screen.exitonclick()