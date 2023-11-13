from random import randint


def guess_the_pick(pick, count):

    guess_count = count

    while not guess_count == 0:

        guess = int(input("Enter your guess: "))

        if guess < pick:
            print(f"{guess} is too low, guess again")
            guess_count -= 1
            print(f"You have {guess_count} guesses remain")
        elif guess > pick:
            print(f"{guess} is too high, guess again")
            guess_count -= 1
            print(f"You have {guess_count} guesses remain")
        elif guess == pick:
            print(f"Congratulations, the number I picked was {pick} as you guessed")
            break
    if guess_count == 0:
        try_again = input("Would you like to try to play the game again on easy mode, yes or no: ").lower
        if try_again == "yes":
            guess_the_pick(pick, 10)
        else:
            return


PICKED_NUMBER = randint(1, 100)

print("Let's play Number Wizard, I'll pick a number and you, the user, will try to guess it.")
print("The number I will pick will be between 1 and 100.")
level = input("Would you like to play the game on easy or hard mode: ").lower()

if level == "easy":
    guess_the_pick(PICKED_NUMBER, 10)
elif level == "hard":
    guess_the_pick(PICKED_NUMBER, 5)
else:
    print("Invalid difficulty level entry")

