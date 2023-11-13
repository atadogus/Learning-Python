from turtle import Turtle


class Racket(Turtle):

    def __init__(self, pos_x, pos_y, screen_height):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("square")
        self.color("white")
        self.shapesize(0.75, 4.50)
        self.starting_x_pos = pos_x
        self.starting_y_pos = pos_y
        self.goto(pos_x, pos_y)
        self.screen_height = screen_height

    def move_up(self):
        self.speed("fastest")
        self.setheading(90)  # this method allows the user to decide the direction in which the turtle object will move
        self.forward(30)
        self.check_out_of_bound_collision(self.xcor(), self.screen_height)

    def move_down(self):
        self.speed("fastest")
        self.setheading(270)
        self.forward(30)
        self.check_out_of_bound_collision(self.xcor(), self.screen_height)

    def racket_control(self, screen, is_player_1):
        screen.listen()
        if is_player_1:
            screen.onkeypress(fun=self.move_up, key="w")
            screen.onkeypress(fun=self.move_down, key="s")
        else:
            screen.onkeypress(fun=self.move_up, key="Up")
            screen.onkeypress(fun=self.move_down, key="Down")

    def check_out_of_bound_collision(self, pos_x, height):
        delta = 20.0 * 4.5 / 2.0
        if self.ycor() < delta - height / 2:
            self.speed("fastest")
            self.goto(pos_x, delta - height / 2)
        if self.ycor() > height / 2 - delta:
            self.speed("fastest")
            self.goto(pos_x, height / 2 - delta)

    def refresh(self):
        self.goto(self.starting_x_pos, self.starting_y_pos)