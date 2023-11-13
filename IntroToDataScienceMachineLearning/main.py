import numpy
from matplotlib import pyplot, cm
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error  # inbuilt method to calculate mse


def my_mean_squared_error(y_value, y_hat_value):
    """Returns the mean square error value"""

    # numpy.average((y_value - y_hat_value)**2, axis=0) same as the below method
    return sum((y_value - y_hat_value)**2)/len(y_value)


# working with data and real cost function, mean squared error: a cost function for regression problems

x = numpy.array([0.1, 1.2, 2.4, 3.2, 4.1, 5.7, 6.5]).reshape(7, 1)
y = numpy.array([1.7, 2.4, 3.5, 3.0, 6.1, 9.4, 8.2]).reshape(7, 1)
"""
ValueError: Expected 2D array, got 1D array instead:
array=[0.1 1.2 2.4 3.2 4.1 5.7 6.5].
Reshape your data either using array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample.
"""

regression = LinearRegression()
regression.fit(x, y)

y_hat = regression.intercept_ + regression.coef_ * x

error = mean_squared_error(y, y_hat)
print(error)

"""
pyplot.scatter(x, y, s=50)
pyplot.plot(x, regression.predict(x), color="orange")
pyplot.show()
"""

number_of_thetas = 200
theta_0 = numpy.linspace(start=-1, stop=3, num=number_of_thetas)
theta_1 = numpy.linspace(start=-1, stop=3, num=number_of_thetas)
plot_theta_0, plot_theta_1 = numpy.meshgrid(theta_0, theta_1)

plot_cost = numpy.zeros((number_of_thetas, number_of_thetas))

for i in range(number_of_thetas):
    for j in range(number_of_thetas):
        new_y_hat = plot_theta_0[i][j] + plot_theta_1[i][j] * x
        plot_cost[i][j] = mean_squared_error(y, new_y_hat)


# min_value = plot_cost.min()
# print(min_value)
# ij_min = numpy.unravel_index(plot_cost.argmin(), dims=plot_cost.shape)
# print(ij_min)


figure = pyplot.figure(figsize=[16, 12])
axes = figure.add_subplot(projection="3d")
axes.set_xlabel("Theta 0", fontsize=20)
axes.set_ylabel("Theta 1", fontsize=20)
axes.set_zlabel("Cost - MSE", fontsize=20)
axes.plot_surface(plot_theta_0, plot_theta_1, plot_cost, cmap=cm.hot)
figure.show()
