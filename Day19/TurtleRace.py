from turtle import Turtle, Screen
from random import randint
screen = Screen()
tarr = []
t1 = Turtle("turtle")
t2 = Turtle("turtle")
tarr.append(t1)
tarr.append(t2)
screen.setup(500, 500)
user = screen.textinput("Who will Win", "Red or Blue")
t1.color("blue")
t2.color("red")
t1.penup()
t2.penup()
t1.goto(-245, 50)
t2.goto(-245, -50)

if user:
    race = True

while race:
    for turtle in tarr:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            race = False
            if user == winner:
                print(f"Youve won the bet {winner} won")
            else:
                print("You lost bet")
        turtle.forward(randint(0, 10))


screen.exitonclick()
