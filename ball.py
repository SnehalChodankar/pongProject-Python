from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.create_ball()
        self.x_move = 10
        self.y_move = 10

    def create_ball(self):
        self.shape("circle")
        self.penup()
        self.color("white")

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1
        self.move()
