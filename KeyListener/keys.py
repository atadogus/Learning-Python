from turtle import Turtle, Screen

screen = Screen()
my_turtle = Turtle()
my_turtle.shape("turtle")


def move_forward():
    my_turtle.forward(10)


def move_backward():
    my_turtle.backward(10)


def rotate_right():
    my_turtle.right(10)


def rotate_left():
    my_turtle.right(-10)


def reset():
    screen.reset()


def turtle_control():
    screen.listen()
    screen.onkeypress(fun=move_forward, key='w')  # when adding a function as a parameter, do not add any parenthesis !!!
    screen.onkeypress(fun=move_backward, key='s')
    screen.onkeypress(fun=rotate_right, key="d")
    screen.onkeypress(fun=rotate_left, key="a")
    screen.onkeypress(fun=reset, key="space")


turtle_control()
screen.exitonclick()