from turtle import Turtle
import random

SPEED = "fastest"
STARTING_HEADING = [45, 135, 225, 315]

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed(SPEED)
        self.penup()
        self.goto(0, 0)
        self.setheading(random.choice(STARTING_HEADING))


    def move(self):
        self.forward(10)

    def bounce_horizontal(self):
        current_heading = self.heading()
        self.setheading(360 - current_heading)

    def bounce_against_paddle(self):
        current_heading = self.heading()
        if current_heading == 45 or current_heading == 225:
            self.setheading(90 + current_heading)
        else:
            self.setheading(current_heading - 90)


