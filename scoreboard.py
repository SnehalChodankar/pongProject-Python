from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.hideturtle()
        self.user_1_score = 0
        self.user_2_score = 0
        self.goto(-100, 200)
        self.write(self.user_1_score, align="center", font=("Courier", 50, "bold"))

        self.goto(100, 200)
        self.write(self.user_2_score, align="center", font=("Courier", 50, "bold"))

    def user1_scored(self):
        self.user_1_score += 1
        self.refresh_score()

    def user2_scored(self):
        self.user_2_score += 1
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.user_1_score, align="center", font=("Courier", 50, "bold"))

        self.goto(100, 200)
        self.write(self.user_2_score, align="center", font=("Courier", 50, "bold"))

    def game_over(self, user):
        self.goto(0, 30)
        self.write("GAME OVER",align="center", font=("Courier", 30, "bold"))

        if user == 1:
            self.goto(0, 0)
            self.write("Left Player Wins", align="center", font=("Courier", 20, "bold"))
        else:
            self.goto(0, 0)
            self.write("Right Player Wins", align="center", font=("Courier", 20, "bold"))