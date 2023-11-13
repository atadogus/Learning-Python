from question_model import Question
from data import question_data
from ui import QuizUI
import html

question_bank = []
for question in question_data:
    new_question = Question(html.unescape(question["question"]), question["correct_answer"])
    question_bank.append(new_question)
    # https://www.udemy.com/course/100-days-of-code/learn/lecture/21233042#overview
    # the reason for me to use html.unescape is explained in the above link


# def old_main():
#    while quiz.still_has_questions():
#        quiz.next_question()
#
#    print("You've completed the quiz")
#    print(f"Your final score was: {quiz.score}/{quiz.question_number}")


def main():
    quiz = QuizUI(question_bank)


if __name__ == "__main__":
    main()
