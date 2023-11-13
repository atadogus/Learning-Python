from turtle import Turtle
from random import randint


class Food(Turtle):  # to inherit another class, enter the class name into the parenthesis

    def __init__(self, width, height):
        super().__init__()  # to access all the attributes of the inherited class, we enter this super initiate method in the constructor
        self.shape("circle")
        self.color("red")
        # self.shapesize(stretch_len=0.9, stretch_wid=0.9)
        self.penup()
        self.speed("fastest")  # this command makes the appearance of the food object on the screen immediate
        self.goto(randint(20 - width / 2, -20 + width / 2), randint(20 - height / 2, -20 + height / 2))

    def refresh(self, width, height):
        self.penup()
        self.speed("fastest")
        self.goto(randint(20 - width / 2, -20 + width / 2), randint(20 - height / 2, -20 + height / 2))
