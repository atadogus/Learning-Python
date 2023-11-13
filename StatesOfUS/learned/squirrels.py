import pandas


gray_squirrel_count = 0
cinnamon_squirrel_count = 0
black_squirrel_count = 0

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_data = data["Primary Fur Color"]

for color in color_data:
    if color == "Gray":
        gray_squirrel_count += 1
    elif color == "Cinnamon":
        cinnamon_squirrel_count += 1
    elif color == "Black":
        black_squirrel_count += 1

print(f"black count: {black_squirrel_count}")
print(f"cinnamon count: {cinnamon_squirrel_count}")
print(f"gray count: {gray_squirrel_count}")

color_dict = {
    "Fur color": ["black", "cinnamon", "gray"],
    "Count": [black_squirrel_count, cinnamon_squirrel_count, gray_squirrel_count]
}

color_count_csv = pandas.DataFrame(color_dict)
color_count_csv.to_csv("color_count.csv")