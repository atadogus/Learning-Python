import colorgram  # external package
from turtle import Turtle, Screen
from random import choice, randint

painting_screen = Screen()
painting_screen.colormode(255)

painter = Turtle()
painter.shape("turtle")


def set_initial_position(x_pos, y_pos):
    painter.penup()
    painter.setposition(x_pos, y_pos)
    painter.pendown()


def paint_dots(dot_radius, number_of_colors, dots_in_a_row, number_of_rows):
    painter.hideturtle()
    extracted_colors = colorgram.extract('image.jpg', number_of_colors)  # this method extracts both rgb and hsl colors
    rgb_colors = []
    for color in extracted_colors:
        rgb_colors.append(color.rgb)

    column_step = (2 * 350) / number_of_rows
    forward_step = (2 * 420) / dots_in_a_row

    for pos in range(number_of_rows + 1):

        for row_pos in range(dots_in_a_row + 1):
            painter.pendown()
            painter.dot(dot_radius, choice(rgb_colors))
            painter.penup()
            painter.forward(forward_step)

        painter.penup()
        painter.right(90)
        painter.forward(column_step)
        painter.right(270)
        painter.setx(-420)


set_initial_position(-420, 350)
paint_dots(25, 20, 12, 14)
painting_screen.exitonclick()
