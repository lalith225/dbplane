import turtle
from turtle import Turtle, Screen
import random

my_screen = Screen()
my_screen.setup(width=500, height=400)

user_bet = my_screen.textinput("Make you bet","Enter the color of turtle which one will win?")
is_race = False
color = ["red", "green", "yellow", "orange", "blue", "purple"]
y_position = [-150, -100, -50, 0, 50, 100]
all_turtle = []
for turtle_index in range(0,6):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.color(color[turtle_index])
    new_turtle.shape("turtle")
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race = True
while is_race:
    for single_turtle in all_turtle:
        if single_turtle.xcor() > 230:
            is_race = False
            winning_color = single_turtle.pencolor()
            if user_bet == winning_color:
                print(f"You have won! and The Turtle color is {winning_color}")
            else:
                print(f"You have lost! and The Turtle color is {winning_color}")

        movements = random.randint(1,10)
        single_turtle.forward(movements)



my_screen.exitonclick()

