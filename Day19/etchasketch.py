from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)


def move_left():
    t.left(10)


def move_right():
    t.right(10)


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")
screen.onkey(t.reset, "c")
screen.exitonclick()
