from turtle import Turtle


class Ball(Turtle):

    def __init__(self, speed):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.speed_x = speed
        self.speed_y = speed

    def move(self):
        x_cor = self.xcor() + self.speed_x
        y_cor = self.ycor() + self.speed_y
        self.goto(x_cor, y_cor)

    def bounce(self):
        self.speed_x = -(self.speed_x + 0.1 * self.speed_x)

    def check_boundary_collision(self, height):
        if self.ycor() < 20 - height / 2:
            self.speed_y = - self.speed_y

        if self.ycor() > height / 2 - 20:
            self.speed_y = - self.speed_y

    def refresh(self, speed):
        self.goto(0, 0)
        self.speed_x = speed
        self.speed_y = speed
