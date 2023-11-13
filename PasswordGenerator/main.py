heights = [1.80, 1.70, 1.60, 1.55, 1.60, 1.65, 1.82, 1.81, 1.77, 1.75, 1.70, 1.72, 1.74, 1.78, 1.74, 1.91]
average = 0

# for height in heights: # for each loop
#     average += height

# if I was not using the len() function
length = 0
for height in heights:
    length += 1

for i in range(0, len(heights)): # classic for loop with incrementation
    average += heights[i]

summation = round(sum(heights), 2) # sums all the values in the list, does the same thing as the above defined for loops
average /= len(heights)
average = round(average, 2)

max_height = heights[0]   # max(heights) # gives the max value in the list
min_height = heights[0]   # min(heights) # gives the min value in the list

# manuel way to calculate min and max
for j in range(0, length):
    if heights[j] > max_height:
        max_height = heights[j]
    if heights[j] < min_height:
        min_height = heights[j]

print(heights)
print(length)
print(min_height)
print(max_height)
print(summation)
print(f"The average height of the students is {average}m.")


gauss_sum = int(input("Enter the number till which you want to sum up all the numbers: "))
result = 0
for k in range (1, gauss_sum + 1):
    result += k

print(result)

# adding step size to for loop

#step_size = 0
#for x in range(0, 21, 3):
#    step_size += x
#    print(step_size)

evens_result = 0
for x in range(0, gauss_sum + 1, 2):
    evens_result += x
    print(evens_result)

odds_result = 0
for y in range(0, gauss_sum + 1): # or I could simple start the for loop from 1 instead of 0 to get the sum of all the odd numbers
    if not y % 2 == 0:
        odds_result += y
        print(odds_result)

# fizzbuzz game
print()
for z in range(1, 11):
    if z % 3 == 0 and not z % 5 == 0:
        print("Fizz")
    elif z % 5 == 0 and not z % 3 == 0:
        print("Buzz")
    elif z % 3 == 0 and z % 5 == 0:
        print("FizzBuzz")
    else:
        print(z)
print("\n")
# password generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#password = []

#for a in range(0, nr_letters):
#    random_letter = random.randint(0, len(letters) - 1)
#    password.append(letters[random_letter])

#for b in range(0, nr_symbols):
#    random_symbols = random.randint(0, len(symbols) - 1)
#    password.append(symbols[random_symbols])

#for c in range(0, nr_numbers):
#    random_number = random.randint(0, len(numbers) - 1)
#    password.append(numbers[random_number])

#new_password = "".join(password)
#print(new_password)


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = []
ordered_password = ""

for a in range(0, nr_letters):
    random_letter = random.randint(0, len(letters) - 1)
    password.append(letters[random_letter])
    ordered_password += random.choice(letters)
    # random.choice(letters) method would have given me a random member within letters[] list
    # if password was a string, I could created a new string in the for loop each time it iterates and concatenated it with the password string like given below
    # new_char = random.choice(letters)
    # password += new_char or password += random.choice(letters)

for b in range(0, nr_symbols):
    random_symbols = random.randint(0, len(symbols) - 1)
    password.append(symbols[random_symbols])
    ordered_password += random.choice(symbols)

for c in range(0, nr_numbers):
    random_number = random.randint(0, len(numbers) - 1)
    password.append(numbers[random_number])
    ordered_password += random.choice(numbers)

# if I were to start with a string nevertheless, I could use split() method with the entry ""
# and converted it into a list and then suffle it and afterwards, could have concatenated the members with a for loop

random.shuffle(password) # this command shuffles the order of the variables contained in a list
new_password = "".join(password) # this command concatenates all the variables in a list into a single string attached to the designated string
print(new_password)
print()
print(ordered_password)