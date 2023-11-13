file = open("my_file.txt")  # to be able to conduct file operations on a certain file, we first need to open it

content = file.read()  # this method takes the content of the file and turns it into a string

print(content)

file.close()
# when done with the file, close method is called to prevent any unwanted alterations from occurring on the file,
# and more importantly, to save our computing power

with open("my_file.txt") as file:  # this way of writing works the same way as the above written set of methods
    content = file.read()
    print(content)

with open("my_file.txt", mode="a") as file:  # the default case is r which stands for read only
    file.write("\nall not gone")  # w is for overwriting the content, to extend on the content mode="a" for appending
    # with mode="a" the write method concatenates the new string right at the end of the last word in the text file

# if the file name entered in the open method does not exist, the method than creates a new file with the given name
# However, a new file is only created when mode="w"