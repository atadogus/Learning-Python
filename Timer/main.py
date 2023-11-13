from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
time_text = ""  # making changes on the text variable and than assigning it to the canvas text variable does not work
reps = 0
checks = ""
countdown = None  # None is the null reference in python


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(countdown)  # to be able to cancel a after() method, we need to assign it first
    count_down(0)
    global checks
    checks = ""
    global reps
    reps = 0
    title_text.config(text="Timer", fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    if reps % 2 == 0:
        if reps == 8:
            title_text.config(text="Long Break", fg=GREEN)
            count_down(LONG_BREAK_MIN * 60)
        else:
            title_text.config(text="Short Break", fg=GREEN)
            count_down(SHORT_BREAK_MIN * 60)
    else:
        title_text.config(text="Working", fg=RED)
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# for the countdown method to work properly, instead of declaring a global text variable and changing it,
# I needed to use a preexisting function in the canvas class, namely .itemconfig() to change the time on screen
# using the time library sleep() method and putting it in a while loop while the conditions are met, does not work
# with gui, it collides with the while loop method .mainloop() of the Tkinter. Therefore, there is this Tk() class method
# called .after() whose first argument in milliseconds sets the amount of time to wait before executing the function
# written in it

def count_down(time):
    global checks
    if reps % 2 == 0 and reps > 0:
        checks += "✔"
        check_marks.config(text=checks)

    if time >= 60:
        minutes = floor(time/60)
        seconds = time % 60
        if seconds < 10:
            if minutes >= 10:
                canvas.itemconfig(timer_text, text=str(f"{minutes}:0{seconds}"))
            else:
                canvas.itemconfig(timer_text, text=str(f"0{minutes}:0{seconds}"))
        else:
            if minutes >= 10:
                canvas.itemconfig(timer_text, text=str(f"{minutes}:{seconds}"))
            else:
                canvas.itemconfig(timer_text, text=str(f"0{minutes}:{seconds}"))
    else:
        if time < 10:
            canvas.itemconfig(timer_text, text=str(f"00:0{time}"))
        else:
            canvas.itemconfig(timer_text, text=str(f"00:{time}"))

    time -= 1
    global countdown
    if time >= 0:
        countdown = window.after(1000, count_down, time)
        check_marks.config()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Timer App")
window.geometry("550x400")
window.config(padx=100, pady=50)
window.config(bg=YELLOW)

title_text = Label(text="Timer", font=(FONT_NAME, 36, "bold"), bg=YELLOW, fg=GREEN)
title_text.grid(row=1, column=2)

check_marks = Label(text="", font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
check_marks.grid(row=4, column=2)

canvas = Canvas(width=204, height=226, bg=YELLOW, highlightthickness=0)
# the default background color of the canvas is white so it needs to change as well to match with the window background
# "highlightthickness=0" is used to get rid of the white frame that appears after matching the background colors
tomato = PhotoImage(file="tomato.png")
canvas.create_image(102, 113, image=tomato)
timer_text = canvas.create_text(102, 125, text="00:00", fill=YELLOW, font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

start_button = Button(text="Start", font=(FONT_NAME, 12, "bold"), bg=GREEN, fg=RED, command=start_timer)
start_button.grid(row=4, column=1)

reset_button = Button(text="Reset", font=(FONT_NAME, 12, "bold"), bg=GREEN, fg=RED, command=reset_timer)
reset_button.grid(row=4, column=3)

window.mainloop()