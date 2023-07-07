from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.score_output()

    def score_output(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"level : {self.score}", align="left", font=FONT)

    def increase_score(self):
        self.score += 1
        self.score_output()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)
