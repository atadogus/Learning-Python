import numpy
from matplotlib import pyplot


def f(x):
    """Quadratic Function"""

    return x ** 2 + x + 1


def df(x):
    """First Derivative of the Above Function"""

    return 2 * x + 1


# Make data

x_1 = numpy.linspace(start=-3, stop=3, num=21)
# this method of numpy creates a sequence of evenly spaced numbers between the given intervals,
# which has as many elements as specified in the num option
print(x_1)


# Gradient Descent

new_x = 3
previous_x = 0
step_multiplier = 0.1
precision = 0.00001  # to stop the loop from running when the desired precision is reached in the results

x_list = [new_x]
slope_list = [df(new_x)]

for n in range(500):
    previous_x = new_x
    gradient = df(previous_x)
    new_x = previous_x - step_multiplier * gradient

    x_list.append(new_x)
    slope_list.append(df(new_x))

    step_size = abs(new_x - previous_x)  # this method is very similar to the Taylor series/
    # when the step size reaches a certain precision, there no longer is a need to run the loop any longer

    if step_size < precision:
        break

print(f"Local minimum occurs at: {new_x}")
print(f"Slope of df(x) value at this point is: {df(new_x)}")
print(f"f(x) value or cost at this point is: {f(new_x)}")

# Creating a plot
pyplot.figure(figsize=[15, 5])

pyplot.subplot(1, 2, 1)  # row, column, index
pyplot.title("My plot")
pyplot.xlim(-3, 3)
pyplot.xlabel("x")
pyplot.ylabel("f(x)")
x_values = numpy.array(x_list)
pyplot.scatter(x_list, f(x_values), color="red", linewidth=5, alpha=0.5)  # superimposing values on the graph to visualize results from the algorithm
pyplot.plot(x_1, f(x_1), color="blue", linewidth=3)

pyplot.subplot(1, 2, 2)
# in order to have the two subplot top to bottom instead of side by side, integer entries for rows and columns
# must be changed to 2, 1 from 1, 2 which means 2 rows 1 column and 1 row 2 columns respectively
pyplot.title("Slope of the function")
pyplot.xlim(-3, 3)
pyplot.xlabel("x")
pyplot.ylabel("df(x)")
pyplot.grid()
pyplot.scatter(x_list, slope_list, color="blue", linewidth=5, alpha=0.5)
pyplot.plot(x_1, df(x_1), color="red", linewidth=3)

pyplot.show()