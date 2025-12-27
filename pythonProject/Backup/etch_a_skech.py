from turtle import Turtle, Screen
my_turtle = Turtle()


def w_forward():
    my_turtle.forward(10)


def s_backward():
    my_turtle.backward(10)


def a_leftward():
    my_turtle.left(10)


def d_rightward():
    my_turtle.right(10)


def c_clearscreen():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()


my_screen = Screen()
my_screen.listen()
my_screen.onkey(key="s", fun=s_backward)
my_screen.onkey(key="w", fun=w_forward)
my_screen.onkey(key="a", fun=a_leftward)
my_screen.onkey(key="d", fun=d_rightward)
my_screen.onkey(key="c", fun=c_clearscreen)
my_screen.exitonclick()
