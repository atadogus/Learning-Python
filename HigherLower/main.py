from Questions import question_list

number_of_question = 0
score = 0

while number_of_question < len(question_list[1]):
    print(question_list[0][number_of_question])
    answer = str(input("a or b: "))
    if answer == question_list[1][number_of_question]:
        score += 1
        number_of_question += 1
        print("Correct, now the next question \n")
    else:
        print(f"Your answer was false, your overall score is {score}")
        break

if score == len(question_list[1]):
    print("Congratulations, you answered all questions right")