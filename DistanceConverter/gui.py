import tkinter  # graphical user interface library


def clicked():
    print("yEahh boyyy")


def change_label():
    my_label["text"] = "button got clicked"


def return_entry():
    # print(tk_input.get())
    my_label["text"] = tk_input.get()


window = tkinter.Tk()
window.title("Learn Tkinter")
window.minsize(1080, 720)

# Label

my_label = tkinter.Label(text="This here is a label", font=("Arial", 24, "bold"))
my_label.pack()  # to display the text written in the label object
my_label.config(text="this is the new text")  # config is a method to make changes in the created label object
my_label["text"] = "changes can be made like this as well"
# parameters of the Label() class are all keys of a dictionary which are a part of the **kwargs


# Button

button = tkinter.Button(text="click", command=return_entry)
button.pack()
# Button() class has a parameter called command which the same as the fun= in the key listener, when the button is
# clicked, it executes the given command


# Entry

tk_input = tkinter.Entry(width=20)
tk_input.pack()
# my_entry = tk_input.get() => assigning the input to a variable did not work, parsing the tk_input.get() into the print() statement worked
# (it will return what is written in the entry box as a string)

window.mainloop()  # it keeps the window on screen running/ this line of code must be at the end of our code to make other commands work

