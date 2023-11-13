# list comprehension: using a single line of code to create a list by using an already existing list

my_list = [1, 2, 3]
print(my_list)

new_list = [number+1 for number in my_list]  # [new item for item in list]
print(new_list)

my_name = "ATA"
print(my_name)

letters_of_my_name = [letter for letter in my_name]  # using a for loop on a single string we can traverse through each character of the string
print(letters_of_my_name)

two_folds = [2 * number for number in range(1, 5)]
print(two_folds)

# conditional list comprehension

new_two_folds = [2 * number for number in range(0, 10) if 2 * number > 4]
print(new_two_folds)

names = ["ata", "taçın", "abdullah", "kazım", "fevzi", "hayrettin"]
short_names = [name for name in names if len(name) < 4]
print(short_names)

numbers_list = [1, 2, 3, 4, 5]
squared_numbers_list = [number * number for number in numbers_list]  # number * number = number ** 2
print(squared_numbers_list)

another_numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers_list = [number for number in another_numbers_list if not number % 2 == 0]
print(odd_numbers_list)