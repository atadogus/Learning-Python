import pandas  # not an inbuilt library

data = pandas.read_csv("weather_data.csv")
type_of_data = type(data)
print(type_of_data)
print("\n")
print(data)

data_dict = data.to_dict()
print("\n")
# there are a bunch of methods which converts the stream of data from a specific file into the data type we specify given in panda library
print(data_dict)

list_of_temperature = data['temp'].to_list()

print(list_of_temperature)

total = sum(list_of_temperature)
average = round(total / len(list_of_temperature), 2)

pandas_average = data["temp"].mean()
# we first specify the column of whose numerical values we want to find the average of
# a method defined in pandas library to calculate the mean value of a specific column of data as long as they are numerical values

print(average)
print(pandas_average)

pandas_mode = data["temp"].mode()
print(f"mode: {pandas_mode}")

pandas_median = data["temp"].median()
print(f"median: {pandas_median}")

pandas_max = data["temp"].max()
print(f"max: {pandas_max}")

# when working with data using pandas, we can specify the column we want to work with in two distinct ways

print(data["condition"])  # treating the data like a dictionary and entering a key value for the specific column

print(data.condition)  # or by doing this

# to work with row data, we need to access our data using a specific column value

print(data[data.day == "Monday"])

# let's find the day with max temperature and extract the data

print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]

temp_in_c = monday.temp
print(temp_in_c)

temp_in_f = 32 + (float(monday.temp) * 9/5)
print(temp_in_f)

# create data frame from scratch

new_data_dict = {
    "students": ["a", "b", "c"],
    "scores": [1, 1, 1]
}

new_data = pandas.DataFrame(new_data_dict)
new_data.to_csv("new_data.csv")  # saves the data as a new csv file
print(new_data)