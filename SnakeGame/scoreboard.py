from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 260)
        self.color("white")
        self.penup()
        self.score = 0
        self.hideturtle()
        self.update_scoreboard()

    def add(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score {self.score}", align="center", font=("Arial", 30, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write("GAME OVER", align="center", font=("Arial", 30, "normal"))


