from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bet", prompt="Which turtle will win the race? Type a color: ").lower()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y=-150
all_turtles = []

for i in range(0, len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y)
    y += 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for new_turtle in all_turtles:
        if new_turtle.xcor() > 230:
            is_race_on = False
            winning_color = new_turtle.pencolor()
            if winning_color == user_bet:
                print(f" You won! The {new_turtle.pencolor()} turtle won at {new_turtle.xcor()}")
            else:
                print(f" You lost! The {new_turtle.pencolor()} turtle won at {new_turtle.xcor()}")

        random_distance = random.randint(0, 10)
        new_turtle.forward(random_distance)


# red = Turtle(shape="turtle")
# red.color("red")
# red.penup()
# red.goto(x=-230, y=-100)
#
# blue = Turtle(shape="turtle")
# blue.color("blue")
# blue.penup()
# blue.goto(x=-230, y=-75)

screen.exitonclick()