from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self, x_coordinate, y_coordinate):
        super().__init__()
        self.score = 0
        self.color("white")  # the text is initially black, have to change the color to see it on the black screen and this definition must come before write() for the text to appear
        self.hideturtle()  # so that only the text will be visible
        self.penup()
        self.goto(x_coordinate, y_coordinate)  # for the turtle to write the text at the location we want,
        self.write(arg=str(self.score), align="center", font=("Arial", 32, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg=str(self.score), align="center", font=("Arial", 32, "normal"))  # to update the score