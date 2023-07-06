import colorgram
from turtle import Turtle, Screen
import random

extracted_color_obj = colorgram.extract("image.jpg", 10)

rgb_tuple_list = []

def print_horizontal():
    for n in range(10):
        turtle.dot(35, random.choice(rgb_tuple_list))
        turtle.up()
        turtle.forward(50)
        turtle.down()

for color_object in extracted_color_obj:
    color_obj_rgb = color_object.rgb
    rgb_values = [color_obj_rgb.r, color_obj_rgb.g, color_obj_rgb.b]
    rgb_tuple = tuple(rgb_values)
    # Instead of creating a list and then transform it to a tuple you can directly create a tuple:
    # rgb_tuple = (color_obj_rgb.r, color_obj_rgb.g, color_obj_rgb.b)
    rgb_tuple_list.append(rgb_tuple)

rgb_tuple_list.pop(0)
turtle = Turtle()
screen = Screen()
screen.colormode(255)
screen.screensize(700,700)
screen.setworldcoordinates(0,0,700,700)
turtle.speed("slow")
turtle.shape("turtle")
turtle.hideturtle()

y = 50
for n in range(10):
    turtle.up()
    turtle.setposition(50, y)
    print_horizontal()
    y += 50

screen.exitonclick()







