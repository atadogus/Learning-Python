import csv  # better way to work with csv data

temperature_values = []

with open("weather_data.csv") as file:
    data = csv.reader(file)
    print(data)  # give the memory location of the data reference

    for row in data:  # we need to parse through to see the data in it
        print(row)

        if row[1].isnumeric():
            # the first row has no string with numeric value written in it,
            # to prevent any errors due to this condition, we eliminate the edge case using this if condition
            temperature_values.append(int(row[1]))

print(temperature_values)

# with open("weather_data.csv") as file:
#    data = file.readlines()
#    print(data)