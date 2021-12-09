#import colorgram
from turtle import Turtle, Screen, ycor
import random
import turtle

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

color_list = [(202, 164, 109), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), 
(145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), 
(14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

def make_dot(color, turtle):
    turtle.dot(20, color)


def print_dots(turtle):
    for _ in range(15):
        turtle.penup()
        color = random.choice(color_list)
        make_dot(color, turtle)
        turtle.forward(50)


def HirstPainting(turtle):
    y = 0
    for _ in range(15):
        print_dots(turtle)
        turtle.home()
        y += 25
        turtle.sety(y)


screen = Screen()
screen.colormode(255)
dots = Turtle()
dots.speed("fastest")
dots.hideturtle()

HirstPainting(dots)

screen.exitonclick()