from turtle import Turtle
import random

COLORS = ["red", "blue", "green", "yellow"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh()

    def refresh(self):
        self.color(COLORS[random.randint(0, 3)])
        self.speed("fastest")
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))
