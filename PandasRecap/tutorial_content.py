import pandas as pd

data = pd.read_csv('lsd_math_score_data.csv')
onlyMathScores = data['Avg_Math_Test_Score']
print(onlyMathScores)
data['Test_Subject'] = 'Jennifer Lopez'
data['High_Score'] = 100
print(data)
data['High_Score'] = data['High_Score'] + data['Avg_Math_Test_Score']
print(data)
data['High_Score'] = data['High_Score'] ** 2
print(data)
cleanData = data[['LSD_ppm', 'Avg_Math_Test_Score']]
print(cleanData)
y = data[['Avg_Math_Test_Score']]
X = data[['LSD_ppm']]
print(X)
type(X)
del data['Test_Subject']
print(data)
del data['High_Score']
print(data)

import math

PI = math.pi
E = math.e

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def get_milk():
    print('Open door')
    print('Walk to the store')
    print('Buy milk on the ground floor')
    print('Return with milk galore')


get_milk()


def fill_the_fridge(amount):
    print('Open door')
    print('Walk to the store')
    print('Buy ' + amount + ' cartons on the ground floor')
    print('Return with milk galore')


fill_the_fridge('five')

fill_the_fridge('one thousand')


def milk_mission(amount, destination):
    print('Open door')
    print('Walk to the ' + destination)
    print('Buy ' + amount + ' cartons on the ground floor')
    print('Return with milk galore')


milk_mission('twenty', 'department store')


def times(a, b):
    # result = a*b
    return a*b


test = times(3.14, 5.09)
print(test)


times('Ni',4)


plt.title('Tissue concentration of LSD over time', fontsize=17)
plt.xlabel('Time in Minutes', fontsize=14)
plt.ylabel('Tissue LSD ppm', fontsize=14)
plt.text(x=0, y=-0.5, s='Wagner et al. (1968)', fontsize=12)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

plt.ylim(1,7)
plt.xlim(0,500)

plt.style.use('classic')

# plt.plot(time, LSD, color='#e74c3c', linewidth=3)
plt.show()


regr = LinearRegression()
# regr.fit(LSD, score)
print('Theta1 : ', regr.coef_[0][0])
print('Intercept: ', regr.intercept_[0])
# print('R-Square: ', regr.score(LSD, score))
# predicted_score = regr.predict(LSD)

# Challenge: add title 'Arithmetic vs LSD-25'
# Add label on X Axis 'Tissue LSD ppm'
# Add label on Y Axis 'Performance Score'
plt.title('Arithmetic vs LSD-25', fontsize=17)
plt.xlabel('Tissue LSD ppm', fontsize=14)
plt.ylabel('Performance Score', fontsize=14)
plt.ylim(25, 85)
plt.xlim(1, 6.5)
plt.style.use('fivethirtyeight')

# plt.scatter(LSD, score, color='blue', s=100, alpha=0.7)
# plt.plot(LSD, predicted_score, color='red', linewidth=3)
plt.show()
