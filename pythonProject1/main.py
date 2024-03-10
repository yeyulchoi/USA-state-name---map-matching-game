import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
state_list = data.state.to_list()
states = []
while len(states) <= 3:
    answer_state = screen.textinput(title=f"{len(states)}/50 State correct", prompt="What is another state's name?").title()


    if answer_state == "Exit":
        missing_states = [missed_state for missed_state in state_list if missed_state not in states]
        print(missing_states)
        new_data =pd.DataFrame(missing_states)
        new_data.to_csv("missed_states.csv")
        break
    if answer_state in state_list:
        answer_row = data[data.state == answer_state]
        states.append(answer_state)
        pointer = turtle.Turtle()
        pointer.hideturtle()
        pointer.penup()
        pointer.goto(int(answer_row.x.iloc[0]), int(answer_row.y.iloc[0]))
        pointer.write(answer_state)


















