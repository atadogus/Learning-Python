from tkinter import Tk, Button, Canvas, PhotoImage
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WAITING_TIME: int = 2000  # in ms


class QuizUI(QuizBrain):
    """
    The quiz UI is a game ai which uses graphical user interface instead of command prompt to interact with the user,
    therefore it inherits QuizBrain class
    """

    def __init__(self, q_list: list):
        """Creates a quiz app UI after instantiation of the class"""

        super().__init__(q_list)

        self.window = Tk()
        self.window.title = "Quizlet App"
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        self.question_card = Canvas(width=800, height=500)
        self.question_card.config(highlightthickness=0)
        self.question_display = self.question_card.create_text(
            400, 250,
            width=750,  # the width argument sets the boundaries of the text object in the canvas
            text="Question", fill=THEME_COLOR, font=("Ariel", 18, "italic"))
        self.question_card.grid(row=0, column=0, columnspan=3, rowspan=4)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.press_true)
        self.true_button.grid(row=5, column=2)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.press_false)
        self.false_button.grid(row=5, column=0)

        self.next_question()

        self.window.mainloop()
        # No code written after this method will work until the mainloop is terminated, that is why I had problems when
        # I called the next_question() method in the main file since it needed to wait for the mainloop to be terminated
        # in order to be executed

    def press_true(self):

        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.true_button.update()
        self.false_button.update()

        self.check_answer(user_answer="true")
        self.question_card.after(WAITING_TIME, self.next_question())

    def press_false(self):

        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.true_button.update()
        self.false_button.update()

        self.check_answer(user_answer="false")
        self.question_card.after(WAITING_TIME, self.next_question())

    # override
    def next_question(self):
        """Displays the next question"""

        if self.still_has_questions():
            self.current_question = self.question_list[self.question_number]
            self.question_number += 1
            self.question_card.itemconfig(self.question_display,
                                          text=f"Q.{self.question_number}: {self.current_question.question_text}")
        else:
            print(f"Your total score is: {self.score}/{self.question_number}")

    # override
    def check_answer(self, user_answer: str):
        """Compares the user answer with the real answer for the question"""

        correct_answer = self.current_question.question_answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            self.question_card.itemconfig(self.question_display,
                                          text=f"You got it right!\nYour current score is: {self.score}/{self.question_number}")
        else:
            self.question_card.itemconfig(self.question_display,
                                          text=f"That's wrong.\nYour current score is: {self.score}/{self.question_number}")

        self.true_button.config(state="normal")
        self.false_button.config(state="normal")
        self.true_button.update()
        self.false_button.update()
