from tkinter import *


def converter():
    miles = float(mile_input.get())
    km = round(miles * 1.61, 2)
    km_value["text"] = str(km)
    pass


window = Tk()
window.title("Mile/Km Converter")
window.minsize(300, 120)

top_left = Label(text="")
top_left.grid(row=0, column=0)

km_text = Label(text="Km", font=("Arial", 12, "bold"))
km_text.grid(row=8, column=8)

km_value = Label(text="no input yet", font=("Arial", 12, "bold"))
km_value.grid(row=8, column=6)

mile_text = Label(text="Miles", font=("Arial", 12, "bold"))
mile_text.grid(row=6, column=8)

mile_input = Entry()
mile_input.grid(row=6, column=6)

convert_button = Button(text="Convert", command=converter)
convert_button.grid(row=10, column=6)

bottom_right = Label(text="")
bottom_right.grid(row=10, column=10)

window.mainloop()