from tkinter import *
from tkinter import messagebox
from password_generator import generate_password
import json


def save_password():
    website = webpage_entry.get()
    email = username_entry.get()
    password = password_entry.get()

    if len(website) < 1 or len(email) < 1 or len(password) < 0:
        messagebox.showinfo(message="Invalid Entry")

    else:
        is_ok = messagebox.askokcancel\
            (title=webpage_entry.get(),
             message=f"email: {username_entry.get()}, \npassword: {password_entry.get()} \nDo you want to save this password")

        if is_ok:
            password_data = {website: {"email": email, "password": password}}

            try:
                with open("passwords.json", mode="r") as input_file:
                    json_input = json.load(input_file)
                    json_input.update(password_data)  # to append the json data at hand
                    # update method includes the new entry by appending the initial variable type coded into the json file, in this case,
                    # this method will add new key:value pairs into the existing dictionary
            except FileNotFoundError:
                pass

            try:
                with open("passwords.json", mode="w") as output_file:
                    json.dump(json_input, output_file, indent=4)  # the variable you want write into json file and the file in which you want to write into
                    # "indent=n", with n being a positive integer, reformats the parsing of the json data
            except NameError:
                with open("passwords.json", mode="w") as output_file:
                    json.dump(password_data, output_file, indent=4)  # if no file is created yet, these lines of codes will create a new .json file


def display_password():
    password_entry.delete(0, "end")
    new_password = str(generate_password())
    password_entry.insert(0, new_password)


def search_password():
    website = webpage_entry.get()
    if len(website) > 0:
        try:
            with open("passwords.json", mode="r") as input_file:
                json_input_to_search = json.load(input_file)
        except FileNotFoundError:
            pass
        else:
            for key in json_input_to_search.keys():  # converts the dictionary of dictionaries into a tuple of dictionaries which can be easily parsed by the for loop
                if key == website:
                    messagebox.showinfo(title=website, message=f"email/username: {json_input_to_search[website]['email']}, \npassword: {json_input_to_search[website]['password']}")
                    return
                else:
                    messagebox.showinfo(title="Error", message="No entries for the website is found")
                    return


window = Tk()
window.title("Password App")
window.config(padx=50, pady=50)

canvas = Canvas(width=202, height=190, highlightthickness=0)
lock = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=lock)
canvas.grid(column=2, row=0)

webpage_label = Label(text="Website")
webpage_label.grid(column=1, row=1)
webpage_entry = Entry(width=35)
webpage_entry.grid(column=2, row=1, columnspan=2)
search_button = Button(text="Search", command=search_password, width=20)
search_button.grid(row=1, column=4)

username_label = Label(text="Email/Username")
username_label.grid(column=1, row=2)
username_entry = Entry(width=35)
username_entry.grid(column=2, row=2, columnspan=2)

password_label = Label(text="Password")
password_label.grid(row=3, column=1)
password_entry = Entry(width=35)
password_entry.grid(column=2, row=3, columnspan=2)
generate_button = Button(text="Generate Password", command=display_password, width=20)
generate_button.grid(column=4, row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=2, row=4, columnspan=2)

window.mainloop()
