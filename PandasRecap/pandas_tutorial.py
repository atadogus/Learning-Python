import pandas

data = pandas.read_csv("csv_data/lsd_math_score_data.csv")

math_scores = data["Avg_Math_Test_Score"]
print(type(math_scores))

# creating a new column in the data frame using pandas / not in the csv file
data["Test_Subject"] = "Social Sciences"
print(data)

data["High_Scores"] = [score + 100.0 for score in data["Avg_Math_Test_Score"]]  # adding extra 100 points to each score in the data frame
print(data)

data["High_Scores"] = data["High_Scores"] ** 2
# simply applying the operation on the whole series is also an
# option instead of using comprehension like above
print(data)

# extracting a smaller data frame from the initial data frame instead of just extracting a single series
# lsd_vs_score = ["LSD_ppm", "Avg_Math_Test_Score"]
# lsd_vs_score_data = data[lsd_vs_score]
lsd_vs_score_data = data[["LSD_ppm", "Avg_Math_Test_Score"]]
# -> this method can be used for extracting a single column as a data frame instead of a series which will prove useful in the future
print(lsd_vs_score_data)

del data["Test_Subject"]  # to delete a column
print(data)
