import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun= player.move, key="Up")

game_is_on = True
loop_number = 0

while game_is_on:

    loop_number += 1

    if loop_number % 6 == 0:
        car_manager.create_car()

    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()

    #Detect collision between turtle and car, print Game Over:

    for cars in car_manager.all_cars:
        if cars.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    #Detect player reaching the other side:

    if player.is_at_finish_line():
        player.reset_position()
        scoreboard.increase_score()
        car_manager.increase_speed()

screen.exitonclick()
