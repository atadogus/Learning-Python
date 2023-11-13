from turtle import Screen, Turtle
from enum import Enum, auto


class Direction(Enum):
    RIGHT = auto()
    LEFT = auto()
    UP = auto()
    DOWN = auto()


class Snake:
    offset = -20

    def __init__(self):
        self.snake_head = Turtle()
        self.snake_head.shape("square")
        self.snake_head.color("dark green")
        self.snake_head.penup()
        self.snake_body = [self.snake_head]
        self.direction = Direction.RIGHT
        offset = -20
        for _ in range(2):
            self.snake_piece = Turtle()
            self.snake_piece.shape("square")
            self.snake_piece.color("green")
            self.snake_piece.penup()
            self.snake_piece.setx(offset)
            self.snake_body.append(self.snake_piece)
            offset -= 20

    def turn_right(self):
        if self.direction == Direction.RIGHT:
            return
        else:
            if self.direction == Direction.UP:
                self.snake_body[0].right(90)
                self.direction = Direction.RIGHT
            elif self.direction == Direction.DOWN:
                self.snake_body[0].left(90)
                self.direction = Direction.RIGHT
            elif self.direction == Direction.LEFT:
                return

    def turn_left(self):
        if self.direction == Direction.LEFT:
            return
        else:
            if self.direction == Direction.UP:
                self.snake_body[0].left(90)
                self.direction = Direction.LEFT
            elif self.direction == Direction.DOWN:
                self.snake_body[0].right(90)
                self.direction = Direction.LEFT
            elif self.direction == Direction.RIGHT:
                return

    def turn_up(self):
        if self.direction == Direction.UP:
            return
        else:
            if self.direction == Direction.RIGHT:
                self.snake_body[0].left(90)
                self.direction = Direction.UP
            elif self.direction == Direction.LEFT:
                self.snake_body[0].right(90)
                self.direction = Direction.UP
            elif self.direction == Direction.LEFT:
                return

    def turn_down(self):
        if self.direction == Direction.DOWN:
            return
        else:
            if self.direction == Direction.LEFT:
                self.snake_body[0].left(90)
                self.direction = Direction.DOWN
            elif self.direction == Direction.RIGHT:
                self.snake_body[0].right(90)
                self.direction = Direction.DOWN
            elif self.direction == Direction.UP:
                return

    def move(self):
        for body_index in range(len(self.snake_body) - 1, 0, -1):
            update_x_pos = self.snake_body[body_index - 1].xcor()
            update_y_pos = self.snake_body[body_index - 1].ycor()
            self.snake_body[body_index].goto(update_x_pos, update_y_pos)
            # instead of moving each piece individually, each piece will allocate itself into the location of the piece coming before it, only the head will move
        self.snake_body[0].forward(20)
