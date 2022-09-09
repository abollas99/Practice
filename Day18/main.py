from turtle import Turtle, Screen, colormode
from random import randint


tim = Turtle()
colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


for n in range(0, 91):
    color = random_color()
    tim.speed(0)
    tim.pencolor(color)
    tim.circle(100)
    tim.setheading(n * 4)

screen = Screen()
screen.exitonclick()
