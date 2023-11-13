from turtle import Turtle, Screen
from random import randint


width = 800
height = 600
finish_pos = (width/2) - 30
race_on = False

colors = ["orange", "red", "green", "yellow", "purple", "blue"]

screen = Screen()
screen.setup(width, height)

offset = 30
starting_x_pos = offset - (width/2)
starting_y_pos = 125

turtles = []

for color in colors:
    racing_turtle = Turtle()
    racing_turtle.shape("turtle")
    racing_turtle.color(color)
    racing_turtle.penup()
    racing_turtle.setx(starting_x_pos)
    racing_turtle.sety(starting_y_pos)
    starting_y_pos -= 50
    turtles.append(racing_turtle)

bet = screen.textinput(title="Make your bet", prompt="Which colour will win: ")
print(bet)

if bet:
    race_on = True

while race_on:
    for turtle in turtles:
        if turtle.xcor() < finish_pos:
            turtle.forward(randint(20, 50))
        else:
            wining_color = turtle.color()[0]
            race_on = False
            break


if bet == wining_color:
    print("You won")
else:
    print(f"You lost, the winner is {wining_color}")

screen.exitonclick()
