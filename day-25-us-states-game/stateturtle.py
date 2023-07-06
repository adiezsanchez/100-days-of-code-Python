from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 10, "bold")


class Stateturtle(Turtle):

    def __init__(self, state_guess, coordinates):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.correct_state = state_guess
        self.coordinates = coordinates
        self.move_to()

    def move_to(self):
        self.goto(self.coordinates)
        self.write(f"{self.correct_state}", align=ALIGNMENT, font=FONT)
