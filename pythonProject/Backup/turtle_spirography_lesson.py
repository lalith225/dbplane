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

def draw_spirography(number_of_side):
    for i in range(int(360/number_of_side)):
        turtle.circle(100)
        current_heading = turtle.heading()
        turtle.setheading(current_heading+number_of_side)
        turtle.circle(100)
        turtle.pencolor(generate_color())

draw_spirography(5)
my_screen = Screen()
my_screen.exitonclick()