from data import question_data
from question_model import Question


class Quiz:
    number_of_questions = len(question_data)
    question_number = 0
    current_question = Question(question_number)
    right_answers = 0

    while question_number < number_of_questions:
        print(current_question.question)
        answer_to_question = input("True or false: ").capitalize()
        question_number += 1

        if answer_to_question == current_question.answer:
            right_answers += 1

        print(f"Your score: {right_answers}/{question_number}")

        if question_number < number_of_questions:  # to prevent a bug
            current_question = Question(question_number)

    print(f"Your total score is {right_answers}/{question_number}")