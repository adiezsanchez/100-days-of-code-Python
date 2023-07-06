from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Generates the screen and paints the discontinuous line in the middle
screen = Screen()
screen.setup(width=600, height=400)
screen.bgcolor("black")
screen.title("PONG")

turtle = Turtle()
turtle.hideturtle()
turtle.speed("fastest")
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.pencolor("white")
turtle.pensize(3)
screen.tracer(0)

# This loop generates the discontinuous line separating the screen
while turtle.ycor() < 200:
    turtle.setheading(90)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
    turtle.forward(10)

# Creation of the 2 paddles on each side of the screen
scoreboard1 = Scoreboard(x_cor= -30)
scoreboard2 = Scoreboard(x_cor= 30)
paddle1 = Paddle(x_cor=-280, y_cor=-20)
paddle2 = Paddle(x_cor=280, y_cor=-20)

# Generation of the ball object
ball = Ball()

# Allowing the control of the paddles
screen.listen()
screen.onkeypress(fun=paddle1.go_up, key="w")
screen.onkeypress(fun=paddle1.go_down, key="s")
screen.onkeypress(fun=paddle2.go_up, key="Up")
screen.onkeypress(fun=paddle2.go_down, key="Down")

# Game logic
game_on = True

while game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # Detect collision with horizontal walls
    if ball.ycor() > 190 or ball.ycor() < -190:
        ball.bounce_horizontal()

    # Detect collision with paddle1
    for segments in paddle1.segments:
        if ball.distance(segments.position()) < 20:
            ball.bounce_against_paddle()

    # Detect collision with paddle2
    for segments in paddle2.segments:
        if ball.distance(segments.position()) < 20:
            ball.bounce_against_paddle()

    # Detect collision with vertical walls and update score of corresponding paddle:
    if ball.xcor() > 300:
        scoreboard1.increase_score()
        ball.hideturtle()
        ball = Ball()

    if ball.xcor() < -300:
        scoreboard2.increase_score()
        ball.hideturtle()
        ball = Ball()

    # Trigger GAME OVER when any of the scoreboards are == 3:
    if scoreboard1.score == 3:
        scoreboard1.winner = 1
        scoreboard1.game_over()
        game_on = False

    if scoreboard2.score == 3:
        scoreboard2.winner = 2
        scoreboard2.game_over()
        game_on = False

screen.exitonclick()
