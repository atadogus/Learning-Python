from tkinter import Tk, Canvas, PhotoImage, Button
from pandas import *
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
list_of_french_words = []
list_of_english_words = []
waiting_time: int = 3000  # in ms
word_index: int = -1


def create_word_pairings():
    """Create a dictionary of French-English word translations using the french_words csv file"""

    global list_of_french_words
    global list_of_english_words

    if len(list_of_french_words) == 0 and len(list_of_english_words) == 0:
        try:
            list_of_words = read_csv("data/remaining_words_to_learn.csv")
        except FileNotFoundError:
            list_of_words = read_csv("data/french_words.csv")

        list_of_french_words = [row.French for (index, row) in list_of_words.iterrows()]
        list_of_english_words = [row.English for (index, row) in list_of_words.iterrows()]


def display_word():
    """Chooses a word from the list of words to be displayed on the UI"""

    global word_index
    wrong_button.config(state="disabled")
    right_button.config(state="disabled")
    wrong_button.update()
    right_button.update()

    try:
        chosen_french_word = choice(list_of_french_words)
    except IndexError:
        print("The list length is 0")
    else:
        word_index = list_of_french_words.index(chosen_french_word)
        flash_card.itemconfig(flash_card_image, image=front_image)
        flash_card.itemconfig(title_display, text="French")
        flash_card.itemconfig(word_display, text=chosen_french_word)
        # https://www.codegrepper.com/code-examples/python/how+to+change+text+in+a+canvas+tkinter

    # sleep(waiting_time)
    """
    Using sleep method from time module jeopardizes the running of the Tkinter UI, since the window created
    using the Tk() already has it's own running time. Instead of using time.sleep(), it is better to use
    after() function present in the Tkinter module, else wise, when using the sleep method, the code before
    it, which makes changes in the UI does not work
    https://stackoverflow.com/questions/10393886/tkinter-and-time-sleep
    """
    flash_card.after(waiting_time, display_translation)
    # display_translation(word_index)


def display_translation():

    flash_card.itemconfig(flash_card_image, image=back_image)
    flash_card.itemconfig(title_display, text="English")
    flash_card.itemconfig(word_display, text=list_of_english_words[word_index])

    wrong_button.config(state="normal")
    right_button.config(state="normal")
    wrong_button.update()
    right_button.update()


def press_thick():

    list_of_french_words.remove(list_of_french_words[word_index])
    list_of_english_words.remove(list_of_english_words[word_index])
    display_word()


def create_new_csv():
    # list_of_french_words.insert(0, "French")
    # list_of_english_words.insert(0, "English")
    # words_not_learned = dict(zip(list_of_french_words, list_of_english_words))
    words_not_learned = {"French": list_of_french_words, "English": list_of_english_words}
    french_words_to_learn = pandas.DataFrame(words_not_learned)
    french_words_to_learn.to_csv("data/remaining_words_to_learn.csv", index=False)


if __name__ == '__main__':

    create_word_pairings()

    window = Tk()
    window.title = "Flash Cards"
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

    cross_image = PhotoImage(file="images/wrong.png")
    wrong_button = Button(image=cross_image, highlightthickness=0, command=display_word)
    wrong_button.grid(row=5, column=0)

    tick_mark_image = PhotoImage(file="images/right.png")
    right_button = Button(image=tick_mark_image, highlightthickness=0, command=press_thick)
    right_button.grid(row=5, column=2)

    front_image = PhotoImage(file="images/card_front.png")
    back_image = PhotoImage(file="images/card_back.png")

    flash_card = Canvas(height=526, width=800)
    flash_card_image = flash_card.create_image(400, 263, image=front_image)
    flash_card.config(bg=BACKGROUND_COLOR, highlightthickness=0)
    title_display = flash_card.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
    word_display = flash_card.create_text(400, 263, text="Text", font=("Ariel", 60, "bold"))
    flash_card.grid(row=0, column=0, columnspan=3, rowspan=4)

    window.mainloop()

    create_new_csv()
