from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 40, "bold")


class Scoreboard(Turtle):

    def __init__(self, x_cor):
        super().__init__()
        self.x_cor = x_cor
        self.score = 0
        self.winner = ""
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(self.x_cor, 130)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Player {self.winner} wins", align=ALIGNMENT, font=FONT)