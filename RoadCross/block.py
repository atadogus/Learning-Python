from turtle import Turtle
from random import choice, randint
from colors_list import colors
from positions_list import y_positions, x_positions


class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(choice(colors))
        self.shapesize(stretch_wid=1.25, stretch_len=2.5)
        self.x_pos = choice(x_positions)
        self.y_pos = choice(y_positions)
        self.goto(self.x_pos, self.y_pos)

    def move(self):
        self.x_pos -= randint(10, 15)
        self.goto(self.x_pos, self.y_pos)
