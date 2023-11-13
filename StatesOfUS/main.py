import pandas
from turtle import Turtle, Screen
from state import State
from time import sleep

screen_width = 724
screen_height = 491
game_screen = Screen()
game_screen.title("Name the States")
game_screen.setup(screen_width, screen_height)
game_screen.bgpic("blank_states_img.gif")

game_on = True

states_data = pandas.read_csv("50_states.csv")

state_names = states_data["state"].to_list()
states_x_cor = states_data["x"].to_list()
states_y_cor = states_data["y"].to_list()
states_count = 0
guessed_states = []

while game_on:
    sleep(0.1)

    entered_name = game_screen.textinput(title=f"{states_count}/50 States Correct", prompt="Enter state name: ").title()

    if entered_name == "Exit":
        # for name in state_names:
        #    if name not in guessed_states:
        #        missing_states.append(name)
        missing_states = [name for name in state_names if name not in guessed_states]  # does the same thing as the above given comment
        learn = pandas.DataFrame(missing_states)
        learn.to_csv("states_to_learn.csv")

        game_on = False

    else:
        for index in range(len(state_names)):
            if state_names[index] == entered_name:
                x_cor = states_x_cor[index]
                y_cor = states_y_cor[index]
                state = State(x_cor, y_cor, entered_name)
                guessed_states.append(state_names[index])
                states_count += 1
                break

    if states_count == 50:
        game_on = False

    game_screen.update()

if states_count == 50:
    print("You know all the states")

game_screen.exitonclick()
