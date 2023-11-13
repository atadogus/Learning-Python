import numpy
from matplotlib import pyplot, cm  # cm stands for colour map
from sympy import symbols, diff


def f(x, y):
    """2d function"""

    return 1 / (3 ** (-x**2 - y**2) + 1)


def dfx(x_value, y_value):
    """Partial derivative with respect to x"""

    x, y = symbols("x, y")

    return diff(f(x, y), x).evalf(subs={x: x_value, y: y_value})


def dfy(x_value, y_value):
    """Partial derivative with respect to y"""

    x, y = symbols("x, y")

    # it is better to write the derivative itself rather than the sympy calculation since it takes more
    # time for the computation when using sympy module
    return diff(f(x, y), y).evalf(subs={x: x_value, y: y_value})


# Batch Gradient Descent

def batch_gradient_descent(learning_rate: float, starting_x: float, starting_y: float, max_iterations: float = float("inf")):
    """Gradient Descent algorithm for multivariable relation"""

    current_point = numpy.array([starting_x, starting_y])
    values_array = current_point.reshape(1, 2)
    current_iteration = 0

    while current_iteration < max_iterations:

        x_gradient = dfx(current_point[0], current_point[1])
        y_gradient = dfy(current_point[0], current_point[1])
        gradients = numpy.array([x_gradient, y_gradient])

        current_point = current_point - learning_rate * gradients
        values_array = numpy.append(values_array, current_point.reshape(1, 2), axis=0)
        # values_array = numpy.concatenate((values_array, current_point.reshape(1, 2)), axis=0) it works the same as the above method

        current_iteration += 1

    return values_array


x_variable = numpy.linspace(start=-2, stop=2, num=200)
y_variable = numpy.linspace(start=-2, stop=2, num=200)

x_variable, y_variable = numpy.meshgrid(x_variable, y_variable)

gradient_descent_values = batch_gradient_descent(learning_rate=0.1, starting_x=1.8, starting_y=1.0, max_iterations=500)


# Generating 3D Plot
figure = pyplot.figure(figsize=[16, 12])  # creating a plot object using the figure method to store the plot
"""
axis = figure.gca(projection="3d")  # gca -> get_current_axes/ this method throws:
"MatplotlibDeprecationWarning: Calling gca() with keyword arguments was deprecated in Matplotlib 3.4. Starting two
minor releases later, gca() will take no keyword arguments. The gca() function should only be used to get the current
axes, or if no axes exist, create new axes with default keyword arguments. To create a new axes with non-default
arguments, use plt.axes() or plt.subplot()." error
solution: https://stackoverflow.com/questions/67095247/gca-and-latest-version-of-matplotlib
"""
axes = figure.add_subplot(projection="3d")
axes.set_xlabel("X", fontsize=20)
axes.set_ylabel("Y", fontsize=20)
axes.set_zlabel("f(x, y) - Cost", fontsize=20)
axes.scatter(gradient_descent_values[:, 0], gradient_descent_values[:, 1], f(gradient_descent_values[:, 0], gradient_descent_values[:, 1]), s=10, color="red")
axes.plot_surface(x_variable, y_variable, f(x_variable, y_variable), cmap=cm.coolwarm, alpha=0.4)
figure.show()
