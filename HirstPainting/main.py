from random import randint
from turtle import Turtle, Screen, colormode

colormode(255)
color_list = [(246, 242, 234), (248, 241, 245), (239, 247, 241), (239, 242, 247), (197, 165, 119), (144, 81, 56), (220, 201, 138), (61, 95, 121), (165, 150, 54), (136, 162, 180), (131, 34, 23), (52, 119, 87), (73, 37, 29), (190, 96, 82), (145, 177, 150), (100, 76, 80), (165, 147, 157), (21, 92, 68), (28, 59, 75), (225, 177, 167), (59, 44, 46), (133, 29, 33), (180, 202, 179), (26, 84, 89), (88, 147, 129), (13, 70, 58), (42, 65, 89), (180, 99, 102), (216, 181, 186), (182, 191, 204)]

t = Turtle()
t.width(15)
t.hideturtle()
t.setheading(225)
t.penup()
t.forward(200)
t.pendown()
t.setheading(0)
t.speed(0)

for m in range(0,10):
    for n in range(0, 10):
        random_color = randint(0, len(color_list) - 1)
        t.pencolor(color_list[random_color])
        t.forward(1)
        t.penup()
        t.forward(30)
        t.pendown()
    t.penup()
    t.backward(310)
    t.setheading(90)
    t.forward(1)
    t.penup()
    t.forward(30)
    t.pendown()
    t.setheading(0)


"""for n in range(0,10):
    random_color = color_list[randint(0, len(color_list) - 1)]
    t.penup()
    t.dot(15, random_color)
    t.forward(30)
"""


screen = Screen()
screen.exitonclick()
