from turtle import Turtle, Screen
from random import choice, randint

screen = Screen()
pen_colors = ["red", "blue", "green", "yellow", "purple", "pink", "orange"]
turns = [0, 90, 180, 270]

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb = (r, g, b)
    return rgb


def draw_square(size):
    timmy_the_turtle.forward(size / 2)
    timmy_the_turtle.right(90)  # degrees
    for _ in range(3):
        timmy_the_turtle.forward(size)
        timmy_the_turtle.right(90)
    timmy_the_turtle.forward(size / 2)


def draw_dashed_line(length, gap_size):
    for _ in range(length):  # using _ in a for loop allows the loop to iterate the code inside for as many times as the defined range value without the need to assign the turn value to any index whatsoever
        timmy_the_turtle.forward(gap_size)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(gap_size)
        timmy_the_turtle.pendown()


def draw_shapes(max_vertices):
    if max_vertices >= 3:
        for vertex in range(3, max_vertices + 1):
            timmy_the_turtle.pencolor(choice(pen_colors))
            for _ in range(vertex):
                timmy_the_turtle.forward(100)
                timmy_the_turtle.right(360 / vertex)
    else:
        return


def random_walk(max_turns, brush_thickness):
    timmy_the_turtle.pensize(brush_thickness)
    screen.colormode(255)  # in order to enter values from 1 to 255
    for _ in range(max_turns):
        timmy_the_turtle.forward(50)
        timmy_the_turtle.right(choice(turns))
        # timmy_the_turtle.pencolor(choice(pen_colors))
        timmy_the_turtle.pencolor(random_color())


def draw_spirograph(radius, number_of_circles):
    timmy_the_turtle.pensize(2)
    screen.colormode(255)
    for _ in range(number_of_circles):
        timmy_the_turtle.pencolor(random_color())
        timmy_the_turtle.circle(radius)
        timmy_the_turtle.right(360/number_of_circles)


draw_spirograph(100, 25)

screen.exitonclick()  # to keep the turtle gui running

# tuple, it is a variable container like a list which is initialized using regular brackets () but when it is initialized, unlike with lists, the variables of a tuple cannot be changed
# For example, an rgb tuple (255, 0, 0, 1) could be created to define red