from turtle import Turtle, Screen

ALIGNMENT = 'left'
FONT_NAME = 'Arial'
FONT_SIZE = 24


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.hideturtle()
        self.screen.tracer(0)
        self.update_score()

    def update_score(self):
        self.write(f"Score:{self.score}", move=False, align=ALIGNMENT, font=(FONT_NAME, FONT_SIZE, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        return self.write(f"Game Over!!!", move=False, align='center', font=(FONT_NAME, FONT_SIZE, 'normal'))


