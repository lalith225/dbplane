from snake_game import Snake
from turtle import Screen, Turtle
from snake_food import Food
from score import Scoreboard
import time


my_screen = Screen()
my_screen.title("Snake")
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.tracer(0)
my_screen.listen()
snake = Snake()
foods = Food()
score = Scoreboard()
my_screen.onkey(snake.snake_up, "Up")
my_screen.onkey(snake.snake_down, "Down")
my_screen.onkey(snake.snake_left, "Left")
my_screen.onkey(snake.snake_right, "Right")



game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(foods) < 15:
        foods.refresh()
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        score.game_over()
        game_is_on = False


my_screen.exitonclick()



