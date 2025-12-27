import turtle
from turtle import Turtle,Screen
import random

my_turtle = Turtle()
turtle.colormode(255)
turtle.pensize(10)
turtle.speed(0)
def generate_color():
    r = random.randint(1,255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    random_color = (r,g,b)
    return random_color


def draw_shape(number_of_side):
    final_angle = int(360 / number_of_side)
    for i in range(number_of_side):
        turtle.forward(100)
        turtle.right(final_angle)


for i in range(3,10):
    draw_shape(i)
    turtle.pencolor(generate_color())
my_screen = Screen()
my_screen.exitonclick()
