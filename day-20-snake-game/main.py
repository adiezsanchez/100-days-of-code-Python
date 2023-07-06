import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


def detect_wall_collision():
    if snake.head.xcor() < -300 or snake.head.xcor() > 300 or snake.head.ycor() < -300 or snake.head.ycor() > 300:
        return True


def detect_tail_collision():
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            return True


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.go_up)
screen.onkey(key="Down", fun=snake.go_down)
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="Right", fun=snake.turn_right)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with walls
    if detect_wall_collision():
        scoreboard.game_over()
        game_on = False

    # Detect collision with tails
    if detect_tail_collision():
        scoreboard.game_over()
        game_on = False

screen.exitonclick()
