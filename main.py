# Create Screen
# Create and move paddle
# Create anotehr paddle
# Create the ball and make it move
# Detact Collision with wall and bounce
# Detact Collision with Paddle
# Detact when paddle misses
# Keep Score
import time
from turtle import Turtle, Screen
import ball
import paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # for smooth reload of screen

user_1 = paddle.Paddle(1)
user_2 = paddle.Paddle(2)
ball = ball.Ball()

screen.listen()

screen.onkey(user_1.up, "w")
screen.onkey(user_1.down, "s")
screen.onkey(user_2.up, "Up")
screen.onkey(user_2.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()  # Used in combination with tracer
    ball.move()

    # Detact collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

screen.exitonclick()
