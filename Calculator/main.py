# simple calculator

def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


operation = input("Enter the operator for the type of operation you want to execute(+, -, *, /): ")

number1 = float(input("Enter the first number: "))

number2 = float(input("Enter the second number: "))

result = 0

if operation == "+":
    result = addition(number1, number2)
elif operation == "-":
    result = subtraction(number1, number2)
elif operation == "*":
    result = multiplication(number1, number2)
elif operation == "/":
    result = division(number1, number2)
else:
    print()

print(f"{number1} {operation} {number2} = {result}")
