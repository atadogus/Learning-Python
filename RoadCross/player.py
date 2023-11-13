from turtle import Turtle


class Player(Turtle):
    def __init__(self, x_pos_start, y_pos_start):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.x_pos_start = x_pos_start
        self.y_pos_start = y_pos_start
        self.goto(self.x_pos_start, self.y_pos_start)
        self.setheading(90)

    def move(self):
        self.forward(20)

    def game_control(self, screen):
        screen.listen()
        screen.onkeypress(self.move, "Up")
