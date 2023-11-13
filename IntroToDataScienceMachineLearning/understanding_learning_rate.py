import numpy
from matplotlib import pyplot

# Understanding Learning Rate


def gradient_descent(derivative_func, initial_guess: float, multiplier: float = 0.01, precision: float = 0.0001, max_step_size: float = float("inf")) -> tuple:
    """
    Gradient Descent algorithm as a function with 4 parameters/ passing default values to make these parameters optional
    """

    current_x = initial_guess
    step_size = initial_guess

    x_list = []
    slope_list = []
    number_of_steps = 0

    while step_size > precision and number_of_steps < max_step_size:
        # Using a while loop can cause the function to run indefinitely, the algorithm may not converge, for example
        # when I set the step size multiplier(the learning rate) to 0.25 and set the max number of steps to 501, the
        # loop ran for 501 times without converging, when picking values such as step size and starting point with this
        # very algorithm, one must be careful

        x_list.append(current_x)

        gradient = derivative_func(current_x)
        slope_list.append(gradient)

        previous_x = current_x
        current_x = previous_x - multiplier * gradient

        step_size = abs(current_x - previous_x)

        number_of_steps += 1

    return current_x, x_list, slope_list


def g(x):
    """Polynomial Function of 4th Degree"""

    return x ** 4 - 4 * (x ** 2) + 5


def dg(x):
    """First Derivative of the Above Function"""

    return 4 * (x ** 3) - 8 * x


# Make data
x_2 = numpy.linspace(-2, 2, 1000)

"""
local_min, values_list, derivatives_list= gradient_descent(derivative_func=dg, initial_guess=1.9, multiplier=0.3, precision=0.001, max_step_size=501)
# when I set the learning rate to 0.3 the function throws OverflowError: (34, 'Result too large'), which means since
# the algorithm does not converge, the current_x value goes towards infinity

print(local_min)


# Creating a plot
pyplot.figure(figsize=[15, 5])

pyplot.subplot(1, 2, 1)  # row, column, index
pyplot.title("My plot")
pyplot.xlim(-2, 2)
pyplot.xlabel("x")
pyplot.ylabel("g(x)")
pyplot.scatter(values_list, g(numpy.array(values_list)), color="red", linewidth=3, alpha=0.5)
pyplot.plot(x_2, g(x_2), color="blue", linewidth=3)

pyplot.subplot(1, 2, 2)
# in order to have the two subplot top to bottom instead of side by side, integer entries for rows and columns
# must be changed to 2, 1 from 1, 2 which means 2 rows 1 column and 1 row 2 columns respectively
pyplot.title("Slope of the function")
pyplot.xlim(-2, 2)
pyplot.xlabel("x")
pyplot.ylabel("dg(x)")
pyplot.grid()
pyplot.scatter(values_list, derivatives_list, color="blue", linewidth=3, alpha=0.5)
pyplot.plot(x_2, dg(x_2), color="red", linewidth=3)

pyplot.show()
"""

# Run gradient descent three times

low_gamma = gradient_descent(derivative_func=dg, initial_guess=3, multiplier=0.0005, precision=0.0001, max_step_size=101)
mid_gamma = gradient_descent(derivative_func=dg, initial_guess=3, multiplier=0.001, precision=0.0001, max_step_size=101)
high_gamma = gradient_descent(derivative_func=dg, initial_guess=3, multiplier=0.002, precision=0.0001, max_step_size=101)

insane_gamma = gradient_descent(derivative_func=dg, initial_guess=1.9, multiplier=0.25, precision=0.0001, max_step_size=101)

# Plotting reduction in cost
pyplot.figure(figsize=[20, 10])
pyplot.title("Cost reduction plot")
pyplot.xlim(0, 100)
pyplot.ylim(0, 50)
pyplot.xlabel("Number of iterations")
pyplot.ylabel("Cost")

# x-axis data: create a list from 0 to number of iterations
x_axis = list(range(0, 101))

# plotting low learning rate
pyplot.plot(x_axis, g(numpy.array(low_gamma[1])), color="blue", linewidth=3)
pyplot.scatter(x_axis, g(numpy.array(low_gamma[1])), color="red", linewidth=3, alpha=0.3)

# plotting mid learning rate
pyplot.plot(x_axis, g(numpy.array(mid_gamma[1])), color="green", linewidth=3)
pyplot.scatter(x_axis, g(numpy.array(mid_gamma[1])), color="red", linewidth=3, alpha=0.3)

# plotting high learning rate
pyplot.plot(x_axis, g(numpy.array(high_gamma[1])), color="red", linewidth=3)
pyplot.scatter(x_axis, g(numpy.array(high_gamma[1])), color="blue", linewidth=3, alpha=0.3)

# plotting insane learning rate
pyplot.plot(x_axis, g(numpy.array(insane_gamma[1])), color="yellow", linewidth=3)
pyplot.scatter(x_axis, g(numpy.array(insane_gamma[1])), color="purple", linewidth=3, alpha=0.5)

pyplot.show()