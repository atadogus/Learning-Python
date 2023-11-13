import pandas
from pandas import DataFrame
import matplotlib.pyplot as pyplot
from sklearn.linear_model import LinearRegression


data = pandas.read_csv("csv_data/lsd_math_score_data.csv")

X = DataFrame(data, columns=["LSD_ppm"])  # same as data[["LSD_ppm"]]
y = DataFrame(data, columns=["Avg_Math_Test_Score"])

regression = LinearRegression()
regression.fit(X, y)  # requires data frames as parameters
prediction = regression.predict(X)


pyplot.figure(figsize=(10, 6))
pyplot.scatter(X, y, alpha=0.3)  # requires data frames as parameters
pyplot.title("Time delay in LSD use", fontsize=20)
pyplot.xlabel("Amount of LSD in ppm")
pyplot.ylabel("Score compared to average")
pyplot.text(x=0, y=1, s="Showing how to add informative text on the graph")

pyplot.xlim(1, 6.5)
pyplot.ylim(25, 85)
# pyplot.style.use("dark_background")  # function used for picking the style of the chart
pyplot.scatter(X, y, color="blue")
# pyplot.plot(X, y, color="green", linewidth=3)
pyplot.plot(X, prediction, color="green", linewidth=3)
# https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
pyplot.show()

print(prediction)
print(regression.coef_)
print(regression.intercept_)
