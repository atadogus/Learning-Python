import tkinter

window = tkinter.Tk()
window.title("Learn Tkinter")
window.minsize(1080, 720)
window.padding(padx=100, pady=100)
# padding() method disallows the use of a certain amount of space from the sides and pushes the gui towards the center


# Label

my_label = tkinter.Label(text="This here is a label", font=("Arial", 24, "bold"))
my_label.config(text="this is the new text")
my_label["text"] = "changes can be made like this as well"
my_label.grid(row=0, column=0)

# my_label.grid(row=0, column=0)  # TclError: cannot use geometry manager pack inside . which already has slaves managed by grid
# the above written error is thrown when I try to use .pack() and .grid() methods in the same window, need to pick one
# of them to let the code function properly


# Button

button = tkinter.Button(text="click", command=print)
# button.pack()
button.place(x=540, y=360)  # place is another layout manager command which places the gui to the given coordinates in the window

# .place() is a very rigid method which requires you to give exact coordinates

# for the given width-height => 1080, 720: 0,0 is the top left vertex of the window and 1080, 720 is the bottom right vertex
# the mid-point in this case is 540, 360


# Entry

tk_input = tkinter.Entry(width=20)
# tk_input.pack()  # pack is a layout manager command and by default, it aligns the given gui to the top center of the window
# by using the parameter side= "...", the alignment of the gui can be changed by entering strings like bottom, left, right...
tk_input.grid(row=1, column=1)

# .grid() method as the name suggests divides the window into grids and when applied on only one gui element, it places
# the gui to the top left corner. When used on several gui elements, it divides the window into grids according to the
# relative row, column positions of the gui given and places them on the window accordingly


window.mainloop()