import time
from turtle import Turtle, Screen
import ball
import paddle
import scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # for smooth reload of screen

user_1 = paddle.Paddle(1)
user_2 = paddle.Paddle(2)
ball = ball.Ball()
scoreboard = scoreboard.Scoreboard()


screen.listen()

screen.onkey(user_1.up, "w")
screen.onkey(user_1.down, "s")
screen.onkey(user_2.up, "Up")
screen.onkey(user_2.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()  # Used in combination with tracer
    ball.move()

    # Detact collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detact Collision with paddle
    if ball.distance(user_2) < 50 and ball.xcor() > 330:
        ball.bounce_x()
    elif ball.distance(user_1) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # Detact Collision with left or right wall
    if ball.xcor() > 380:
        ball.hit_wall()
        scoreboard.user1_scored()
    elif ball.xcor() < -380:
        ball.hit_wall()
        scoreboard.user2_scored()

    if scoreboard.user_1_score == 5:
        scoreboard.game_over(1)
        game_is_on = False
    elif scoreboard.user_2_score == 5:
        game_is_on = False
        scoreboard.game_over(2)


screen.exitonclick()
