from turtle import Turtle

WIDTH = 800
HEIGHT = 600
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, num):
        super().__init__()

        self.create_paddle(num)

        self.score = 0

    def create_paddle(self, num):
        self.shape("square")
        self.color("white")
        self.resizemode("user")
        self.shapesize(5, 1)
        self.penup()
        if num == 1:
            self.setpos(-350, 0)
        else:
            self.setpos(350, 0)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
