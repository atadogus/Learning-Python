from turtle import Turtle, Screen

timmy = Turtle()
my_screen = Screen()
timmy.shape("turtle")
timmy.color("green")
move = 0
timmy.forward(200)

print(my_screen.canvheight)
my_screen.exitonclick()

# to be able to import an external package into our project, we need to go to the following path:
# File/Settings/${project_name}/Python Interpreter and there, we push the plus button to download a defined package
# in the pypi.org by entering it's name in the search table