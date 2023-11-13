import pandas
from pandas import DataFrame
import matplotlib.pyplot as pyplot
from sklearn.linear_model import LinearRegression

data = pandas.read_csv("csv_directory/cost_revenue_clean.csv")

# print(data.describe())

x = DataFrame(data, columns=['production_budget_usd'])
y = DataFrame(data, columns=['worldwide_gross_usd'])

regression = LinearRegression()
regression.fit(x, y)
slope = regression.coef_
intercept = regression.intercept_

pyplot.figure(figsize=(10, 6))
pyplot.scatter(x, y, alpha=0.3)
pyplot.plot(x, regression.predict(x), color="red", linewidth=4)
pyplot.title("Film Gross vs Global Revenue")
pyplot.xlabel("Production Budget($)")
pyplot.ylabel("Worldwide Gross($)")
pyplot.xlim(0, 450000000)
pyplot.ylim(0, 3000000000)
pyplot.show()

regression.score(x, y)  # goodness of fit, R^2
