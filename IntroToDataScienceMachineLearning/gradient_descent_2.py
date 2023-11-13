import numpy
from matplotlib import pyplot


def gradient_descent(derivative_func, initial_guess: float, multiplier: float = 0.01, precision: float = 0.0001) -> tuple:
    """
    Gradient Descent algorithm as a function with 4 parameters/ passing default values to make these parameters optional
    """

    current_x = initial_guess
    step_size = initial_guess

    x_list = []
    slope_list = []

    while step_size > precision:
        x_list.append(current_x)

        gradient = derivative_func(current_x)
        slope_list.append(gradient)

        previous_x = current_x
        current_x = previous_x - multiplier * gradient

        step_size = abs(current_x - previous_x)

    return current_x, x_list, slope_list


def g(x):
    """Polynomial Function of 4th Degree"""

    return x ** 4 - 4 * (x ** 2) + 5


def dg(x):
    """First Derivative of the Above Function"""

    return 4 * (x ** 3) - 8 * x


# Make data
x_2 = numpy.linspace(-2, 2, 1000)

local_min, values_list, derivatives_list = gradient_descent(derivative_func=dg, initial_guess=0.5, multiplier=0.02,
                                                            precision=0.001)
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
