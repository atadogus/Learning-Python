import random

#print("Let's play heads or tails")

#heads_or_tails = str(input("Pick you choice, heads or tails: "))

#coin_flip = random.random() # more then 0.5 means heads, less than 0.5 means tails

#if coin_flip < 0.5:
#    print("tails")
#    if heads_or_tails == "heads":
#        print("You loose this round")
#    elif heads_or_tails == "tails":
#        print("You win this round")
#    else:
#        print("You have entered an invalid value")
#elif coin_flip > 0.5:
#    print("heads")
#    if heads_or_tails == "heads":
#        print("You win this round")
#    elif heads_or_tails == "tails":
#        print("You loose this round")
#    else:
#        print("You have entered an invalid value")

#cards = str(input("Who is gonna pay for the bill: "))
#business_cards_list = cards.split(", ") # splits a string into separate variables using the entry as an indication of where to split and lists them

#print(business_cards_list)

#business_cards_list.append("Onat")
# append is a list method to add a new variable at the end of the list
# explanations of further list methods can be found  https://docs.python.org/3/tutorial/datastructures.html
#print(business_cards_list)

#pick = random.randint(0, len(business_cards_list) - 1)
#payer = business_cards_list[pick]
#print(f"{payer} is gonna pay the bill")

# 🚨 Don't change the code below 👇
# row1 = ["⬜️", "⬜️", "⬜️"]
# row2 = ["⬜️", "⬜️", "⬜️"]
# row3 = ["⬜️", "⬜️", "⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
# coordinates = position.split(", ")

# location_row = int(coordinates[0]) - 1       # int(input("Enter the row coordinate: "))
# location_column = int(coordinates[1]) - 1    # int(input("Enter the column coordinate: "))
# map[location_row][location_column] = "x"


# Write your code above this row 👆

# 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")


moves = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

moves = [moves, paper, scissors]

print("Let's play rock, paper, scissors.")

choice = input("Pick your choice. Rock, paper or scissors: ")

computer_choice = random.randint(1, 3)

if computer_choice == 1:
    if choice == "rock":
        print(f"Player: {moves[0]}")
        print(f"Computer: {moves[0]}")
        print("Draw")
    elif choice == "paper":
        print(f"Player: {moves[1]}")
        print(f"Computer: {moves[0]}")
        print("Win")
    elif choice == "scissors":
        print(f"Player: {moves[2]}")
        print(f"Computer: {moves[0]}")
        print("Lose")
    else:
        print()
elif computer_choice == 2:
    if choice == "rock":
        print(f"Player: {moves[0]}")
        print(f"Computer: {moves[1]}")
        print("Lose")
    elif choice == "paper":
        print(f"Player: {moves[1]}")
        print(f"Computer: {moves[1]}")
        print("Draw")
    elif choice == "scissors":
        print(f"Player: {moves[2]}")
        print(f"Computer: {moves[1]}")
        print("Win")
    else:
        print()
elif computer_choice == 3:
    if choice == "rock":
        print(f"Player: {moves[0]}")
        print(f"Computer: {moves[2]}")
        print("Win")
    elif choice == "paper":
        print(f"Player: {moves[1]}")
        print(f"Computer: {moves[2]}")
        print("Lose")
    elif choice == "scissors":
        print(f"Player: {moves[2]}")
        print(f"Computer: {moves[2]}")
        print("Draw")
    else:
        print()
else:
    print()