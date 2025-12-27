from turtle import Turtle


initial_coordinates = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.create_snake()

    def create_snake(self):
        for i in range(0, 3):
            my_seg = Turtle()
            my_seg.penup()
            my_seg.shape("square")
            my_seg.color("white")
            my_seg.goto(initial_coordinates[i])
            self.segments.append(my_seg)

    def adding_snake(self, position):
        my_seg = Turtle()
        my_seg.penup()
        my_seg.shape("square")
        my_seg.color("white")
        my_seg.goto(initial_coordinates[position])

    def extend(self):
        extend_seg = Turtle()
        self.segments.append(extend_seg)

    # move snake
    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg - 1].xcor()
            y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x, y)
            self.segments[0].forward(10)

    def snake_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def snake_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def snake_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def snake_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

