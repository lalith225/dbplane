import random

import colorgram
import turtle
import random



# rgb_colors = []
# color = colorgram.extract("C:/Users/EIMS/PycharmProjects/pythonProject/image.jpg", 40)
# for colors in color:
#     r = colors.rgb.r
#     g = colors.rgb.g
#     b = colors.rgb.b
#     new_tuple = (r, g, b)
#     rgb_colors.append(new_tuple)

color_list = [(242, 242, 241), (233, 234, 237), (239, 242, 240), (51, 100, 189), (142, 89, 40), (243, 235, 240), (185, 42, 83), (107, 188, 124), (69, 125, 192), (239, 209, 84), (48, 105, 81), (62, 39, 64), (169, 7, 63), (200, 109, 163), (197, 100, 155), (123, 158, 195), (199, 73, 60), (184, 154, 130), (224, 171, 192), (168, 205, 181), (132, 141, 97), (171, 184, 222), (47, 42, 58), (228, 172, 164), (104, 141, 126), (82, 95, 26), (35, 88, 67), (68, 141, 185), (162, 201, 213)]
my_trutle = turtle.Turtle()
turtle.colormode(255)
turtle.speed("fastest")
turtle.penup()
turtle.hideturtle()
turtle.setheading(225)
turtle.forward(250)
turtle.setheading(0)
numbers_of_dots = 100
for dots in range(1, numbers_of_dots+1):
    turtle.dot(20, random.choice(color_list))
    turtle.forward(50)
    if dots%10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)



my_screen = turtle.Screen()
my_screen.exitonclick()

