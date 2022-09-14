import turtle
import pandas
import csv

screen = turtle.Screen()
screen.title("US Map")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(height=491, width=725)
turtle.shape(image)

data = pandas.read_csv(f"50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess the state", prompt="Whats another states name?").title()
    print(answer_state)
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())


screen.exitonclick()
