from turtle import Screen
import pandas as pd

data = pd.read_csv("50_states.csv")
states_column = data["state"]
states_list = states_column.to_list()
states_list_lc = []

for states in states_list:
    state_lc = states.lower()
    states_list_lc.append(state_lc)


class Stateinput(Screen, states_list_lc):

    def __init__(self):
        super().__init__()
        self.states_list_lc = states_list_lc
        self.correct_states = 0
        self.state_guess = textinput(title=f"{self.correct_states}/50 States Correct", prompt="What's another state name?").lower()
        self.update_scoreboard()

    def check_answer(self):

    def update_scoreboard(self):