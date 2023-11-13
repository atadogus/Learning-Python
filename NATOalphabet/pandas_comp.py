import pandas

student_dict = {"students": ["a", "b", "c"], "scores": [80, 82, 67]}

student_data = pandas.DataFrame(student_dict)
print(student_data)

for (key, value) in student_data.items():
    print(value)

# an inbuilt method in pandas library to traverse through data frames => .iterrows()

for (index, row) in student_data.iterrows():
    if row.students == "a":
        print(row.scores)