# find the file on dekstop using absolute path

with open("C:/Users/MONSTER/Desktop/find_me.txt") as file:
    # the paths of files are normally given with backward slashes "\", but when looking for them via commands, forwards slashes "/" are used instead
    content = file.read()
    print(content)

# let's try to find another file using relative path this time, using relative path to find a file on dekstop
# is unnecessary since the file path is completely different from the python file

with open("../../relative_path/find_me_relatively.txt") as file:
    content = file.read()
    print(content)

# each .. takes you to the parent folder containing the current file we are working in, in this case the main.py file

# path of our project D:\PythonRepo\WorkWithTextFiles\main.py
# path of the file we searched for D:\relative_path\find_me_relatively.txt
# we use .. two times consecutively to reach the parent folder which holds both python file
# and the text file we were looking for and from there we started to get to the text file