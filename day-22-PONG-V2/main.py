from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Generates the screen and paints the discontinuous line in the middle
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

l_paddle = Paddle(x_cor=-350)
r_paddle = Paddle(x_cor=350)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=l_paddle.go_up, key="w")
screen.onkeypress(fun=l_paddle.go_down, key="s")
screen.onkeypress(fun=r_paddle.go_up, key="Up")
screen.onkeypress(fun=r_paddle.go_down, key="Down")

# Game logic
game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with horizontal walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with l_paddle:
    if ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    # Detect collision with r_paddle:
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50:
        ball.bounce_x()

    # Detect collision with vertical walls (r_paddle miss) and update score:
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()


    # Detect collision with vertical walls (l_paddle miss) and update score:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()