from turtle import Screen
import pandas as pd
from stateturtle import Stateturtle

data = pd.read_csv("50_states.csv")
states_column = data["state"]
states_list = states_column.to_list()
correct_states_list = []

print(states_list)

screen = Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")

correct_states = 0

while len(correct_states_list) < 50:
    state_guess = screen.textinput(title=f"{correct_states}/50 States Correct",
                                   prompt="What's another state name?").title()

    if state_guess == "Exit":
        # List comprehension alternative
        states_to_learn = [state for state in states_list if state not in correct_states_list]
        # Without list comprehension alternative
#        for state in states_list:
#            if state not in correct_states_list:
#                states_to_learn.append(state)

        states_to_learn_df = pd.DataFrame(states_to_learn)
        states_to_learn_df.to_csv("states_to_study.csv")
        break  # Breaks the loop and exits out of it

    if state_guess in states_list:

        if state_guess in correct_states_list:
            pass
        else:
            correct_states += 1
            correct_states_list.append(state_guess)

        # Access the row corresponding to the state guess value
        state = data[data.state == state_guess]
        # Access the x value (within the x column) within the state guess row
        x_cor = int(state.x)
        # Access the y value (within the x column) within the state guess row
        y_cor = int(state.y)
        coordinates = (x_cor, y_cor)
        state_turtle = Stateturtle(state_guess, coordinates)

