print("Let's try to make a simple program which helps you with splitting the bill")
bill = float(input("Enter the bill: "))
number_of_people = float(input("Enter the number of people who ordered food: "))
bill_split = bill / number_of_people
tip = float(input("Enter the percentage of the tip you would like to leave: "))
bill_final = round(bill_split * (1 + tip/100), 2)
print(f"The total you need to pay is ${bill_final}")

# extra info: type() is a function which gives you the data type of the variable you enter into the parenthesis

# exemplary use of the above explained function

# print(type(bill_final))

# to round floating numbers to certain number of decimal places, this coding is used -> round(3/5, 2) meaning show me
# the result with two decimal places


