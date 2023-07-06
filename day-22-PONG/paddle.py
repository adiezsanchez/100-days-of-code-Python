from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle:

    def __init__(self, x_cor, y_cor):
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.segments = []
        self.create_paddle()

    def create_paddle(self):
        y_coord = self.y_cor
        for i in range(3):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(self.x_cor, y_coord)
            self.segments.append(segment)
            y_coord += 20

    def go_up(self):
        for segments in self.segments:
            segments.setheading(UP)
            segments.forward(MOVE_DISTANCE)


    def go_down(self):
        for segments in self.segments:
            segments.setheading(DOWN)
            segments.forward(MOVE_DISTANCE)

