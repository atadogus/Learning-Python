from enum import Enum, auto
from random import choice


class Hand(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()


options = [Hand.ROCK, Hand.PAPER, Hand.SCISSORS]


def player_choice() -> Hand:
    """Player chooses which of the three options they will go with"""

    my_hand = input("Enter your choice here: ")

    while type(my_hand) is not Hand:

        if my_hand.lower() == "rock":
            my_hand = Hand.ROCK
        elif my_hand.lower() == "paper":
            my_hand = Hand.PAPER
        elif my_hand.lower() == "scissors":
            my_hand = Hand.SCISSORS
        else:
            print(f"{my_hand} is an invalid entry, please try again")
            my_hand = input("Enter your choice here: ")

    return my_hand


def main():

    player_hand: Hand = player_choice()
    p_name = player_hand.name.title()
    print(f"You choose {p_name}")

    computer_hand: Hand = choice(options)
    c_name = computer_hand.name.title()
    print(f"Computer chooses {c_name}")

    match player_hand:
        case Hand.ROCK:
            if computer_hand is Hand.ROCK:
                print("Draw")
            elif computer_hand is Hand.PAPER:
                print(f"{p_name} looses against {c_name}")
            else:
                print(f"{p_name} wins against {c_name}")

        case Hand.PAPER:
            if computer_hand is Hand.ROCK:
                print(f"{p_name} wins against {c_name}")
            elif computer_hand is Hand.PAPER:
                print("Draw")
            else:
                print(f"{p_name} looses against {c_name}")

        case Hand.SCISSORS:
            if computer_hand is Hand.ROCK:
                print(f"{p_name} looses against {c_name}")
            elif computer_hand is Hand.PAPER:
                print(f"{p_name} wins against {c_name}")
            else:
                print("Draw")


if __name__ == '__main__':
    print("Let's play rock-paper-scissors")
    main()
