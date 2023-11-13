import numpy
from matplotlib import pyplot


def h(x):
    """Some polynomial function"""

    return x ** 5 - 2 * (x ** 4) + 2


def dh(x):
    """It's derivative"""

    return 5 * (x ** 4) - 8 * (x ** 3)


# Make data
x_3 = numpy.linspace(start=-2.5, stop=2.5, num=1000)

# Creating a plot
pyplot.figure(figsize=[15, 5])

pyplot.subplot(1, 2, 1)  # row, column, index
pyplot.title("My plot")
pyplot.xlim(-1.2, 2.5)
pyplot.ylim(-1, 4)
pyplot.xlabel("x")
pyplot.ylabel("h(x)")
# pyplot.scatter(values_list, g(numpy.array(values_list)), color="red", linewidth=3, alpha=0.5)
pyplot.plot(x_3, h(x_3), color="blue", linewidth=3)

pyplot.subplot(1, 2, 2)
# in order to have the two subplot top to bottom instead of side by side, integer entries for rows and columns
# must be changed to 2, 1 from 1, 2 which means 2 rows 1 column and 1 row 2 columns respectively
pyplot.title("Slope of the function")
pyplot.xlim(-1.2, 2.5)
pyplot.ylim(-5, 5)
pyplot.xlabel("x")
pyplot.ylabel("dh(x)")
pyplot.grid()
# pyplot.scatter(values_list, derivatives_list, color="blue", linewidth=3, alpha=0.5)
pyplot.plot(x_3, dh(x_3), color="red", linewidth=3)

pyplot.show()
