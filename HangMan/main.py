import random
import hangmanGUI
import hangmanWords

# there are 7 stages in total
print(hangmanGUI.logo)
print("\nWelcome to the Hangman Game, let's try to guess the word")

words = hangmanWords.hangman_words
pick = list(random.choice(words)) # using list method splits the characters of a string and contains them in a list

word = ""
for i in pick:
    word += "_"
print(f"The word you are gonna guess has {len(word)} letters in it")
print(word)
word_container = list(word)

guess_count = 0
stage_count = 6
print(hangmanGUI.stages[stage_count])

while word_container.count('_') > 0 and guess_count < 6:
    guess = str(input("Enter a letter: ")).lower()
    # the lower method is included to make any letter type character entry to be taken as lower case letter
    letter_found = False
    same_letter = False

    for picked in range(len(pick)):
        if word_container[picked] == guess:
            same_letter = True

        elif pick[picked] == guess:
            letter_found = True
            word_container[picked] = guess

    if same_letter:
        print(f"You have already entered this letter, {guess}")

    elif not letter_found:
        guess_count += 1
        guess_remain = 6 - guess_count
        stage_count -= 1
        if guess_remain == 1:
            print("You have only 1 guess remain")
        else:
            print(f"You have {guess_remain} more guesses remain")

    else:
        temporary_container = word_container  # in order to protect the list structure, an auxiliary list is created each time to be concatenated
        word = ""  # assigning an empty string to the word in order to update it properly
        word = word.join(temporary_container)  # the join method concatenates members of a list to the end of a string but in the process, it erases the list
    print(hangmanGUI.stages[stage_count])
    print(word)

if guess_count == 6:
    print("You have lost :(")
    looked_word = "".join(pick)
    print(f"The word we were looking for was: {looked_word}")
else:
    print("Congratulations, you've won")

# in this program, the order of the commands really do play an important role, for example in the picked for loop,
# if I do not check the condition for same letter first, the condition will always remain false since in the case of
# choosing a correct letter, the letter will automatically be assigned by the other if condition and the elif statement
# for the same letter check would be ignored. On the other hand, if I were to write them as two separate if conditions,
# in the case of choosing a correct letter, same letter condition will set to be true every time, even if it is
# the first time the letter is chosen