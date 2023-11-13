my_list = [1, 2, 3, 4]
print(my_list)
print(hex(id(my_list)))

my_list.append(5)
print(my_list)
print(hex(id(my_list)))
# when appended, the memory address of the list does not change, only the internal state of the object has changed

my_other_list = [1, 2, 3, 4]
print(my_other_list)
print(hex(id(my_other_list)))
# although it has the same elements as the other list, this one has a different memory address

my_other_list = my_other_list + [5]  # concatenating two lists
print(my_other_list)
print(hex(id(my_other_list)))
# the memory address in this case has changed since the two lists above are concatenated and a new list was
# created to store the resulting data

my_dict = {"key1": 1, "key2": 2}
print(my_dict)
print(hex(id(my_dict)))

my_dict["key3"] = 3
print(my_dict)
print(hex(id(my_dict)))
# The memory address of the dictionary has not changed

my_tuple = (my_list, my_dict)
print(my_tuple)
print(hex(id(my_tuple)))

my_list.append(6)
print(my_tuple)
print(hex(id(my_tuple)))
# the internal state of one of the elements of the tuple has changed but the tuple itself has not and is still
# pointing to the same memory address


def process(anything: tuple) -> tuple:
    for element in anything:
        if type(element) is list:
            element.append("appended")

    return anything
# "is" is called the identity operator and compares the two objects and gives a boolean value whether the compared
# objects are the same
# "==" is called the equality operator and compares whether the internal state of the two objects(the data) are the same
# is not: negation operator of identity
# != : negation operator of equality

# The "None" object(the null pointer): The object can be assigned to variables to indicate that they are not set,
# i.e an empty value. But the None object is a real object that is managed by Python memory manager. Furthermore, the
# memory manager will always use a shared reference when assigning a variable to None.

# is None: to check whether the object is set or empty, if no data is assigned to the variable, than the statement will
# return True


process(my_tuple)
print(my_tuple)


def concatenate(string: str) -> str:
    return f"Your string '{string}' is concatenated"


my_string = "Hello"
print(my_string)
print(hex(id(my_string)))

print(concatenate(my_string))
print(my_string)
print(hex(id(my_string)))
# my_string, an immutable object, has not changed by the function unlike the list inside the tuple above, which was
# appended after processed by the process function. It is good/safer to use immutable objects to store references, when
# we do not want to alter the internal structure of the object by any function