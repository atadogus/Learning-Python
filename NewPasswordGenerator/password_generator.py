from random import randint, choice, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_length = 12

print("Welcome to the PyPassword Generator!")
nr_symbols = randint(1, 3)
nr_numbers = randint(2, 5)
nr_letters = 12 - (nr_numbers + nr_symbols)


def generate_password():
    password = []
    ordered_password = ""

    for a in range(0, nr_letters):
        random_letter = randint(0, len(letters) - 1)
        password.append(letters[random_letter])
        ordered_password += choice(letters)

    for b in range(0, nr_symbols):
        random_symbols = randint(0, len(symbols) - 1)
        password.append(symbols[random_symbols])
        ordered_password += choice(symbols)

    for c in range(0, nr_numbers):
        random_number = randint(0, len(numbers) - 1)
        password.append(numbers[random_number])
        ordered_password += choice(numbers)

    # if I were to start with a string nevertheless, I could use split() method with the entry ""
    # and converted it into a list and then shuffle it and afterwards, could have concatenated the members with a for loop

    shuffle(password)  # this command shuffles the order of the variables contained in a list
    new_password = "".join(password)
    # this command concatenates all the variables in a list into a single string attached to the designated string
    return new_password
