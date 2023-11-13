from deck import cards
import random


def draw():
    card = random.choice(cards)
    cards.remove(card)
    return card


def calculate_score_player(hand):
    score = 0
    while hand.__contains__("ace") or hand.__contains__("jack") or hand.__contains__("queen") or hand.__contains__(
            "king"):
        if hand.__contains__("ace"):
            hand.remove("ace")
            value = int(input("Do you want it to count as 1 or 11: "))
            if value == 1:
                hand.append(1)
            elif value == 11:
                hand.append(11)
        elif hand.__contains__("jack"):
            hand.remove("jack")
            hand.append(10)
        elif hand.__contains__("queen"):
            hand.remove("queen")
            hand.append(10)
        elif hand.__contains__("king"):
            hand.remove("king")
            hand.append(10)

    for card in hand:
        score += card

    return score


def calculate_score_dealer(hand, other_score):
    score = 0
    ace_removed = False
    times_ace_removed = 0
    # print(hand)
    while hand.__contains__("ace") or hand.__contains__("jack") or hand.__contains__("queen") or hand.__contains__(
            "king"):
        if hand.__contains__("ace"):
            hand.remove("ace")
            ace_removed = True
            times_ace_removed += 1
        elif hand.__contains__("jack"):
            hand.remove("jack")
            hand.append(10)
        elif hand.__contains__("queen"):
            hand.remove("queen")
            hand.append(10)
        elif hand.__contains__("king"):
            hand.remove("king")
            hand.append(10)

    for card in hand:
        score += card

    if ace_removed and times_ace_removed == 2:
        hand.append(11)
        hand.append(1)
        score = 0
        for card in hand:
            score += card
        return score
    elif ace_removed and times_ace_removed == 1:
        if score == 10:
            hand.append(11)
            score = 0
            for card in hand:
                score += card
            return score
        elif 10 > score:
            hand.append(11)
            score = 0
            for card in hand:
                score += card
            return score
        elif score > 10:
            hand.append(1)
            score = 0
            for card in hand:
                score += card
            return score
        else:
            hand.append(1)
            score = 0
            for card in hand:
                score += card
            return score
    return score


def play(hand, name):
    print(f"Playing with {name}")

    game_over = False
    end_turn = False
    hand.append(draw())
    print(hand)
    score = calculate_score_player(hand)
    print(score)

    while score <= 21 or not end_turn:
        if score > 21:
            if hand.__contains__(11):
                print("Make ace 1")
                hand.remove(11)
                hand.append(1)
                score = calculate_score_player(hand)
                print(hand)
                print(score)
            else:
                game_over = True
                break

        next_move = input("Do you want to draw another card or end your turn, 'draw' or 'end': ").lower()
        if next_move == "end":
            end_turn = True
            break
        else:
            hand.append(draw())
            print(hand)
            # score = calculate_score_player(hand)

        score = calculate_score_player(hand)
        print(score)
    if game_over:
        print(f"{name} has busted")
    return score


def play_dealer(hand, score, name):
    print(f"Playing with {name}")

    game_over = False
    end_turn = False
    # hand.append(draw())
    print(hand)
    the_score = calculate_score_dealer(hand, score)
    print(the_score)

    while the_score <= 21 and not end_turn:
        if the_score > 21:
            if hand.__contains__(11):
                print("Make ace 1")
                hand.remove(11)
                hand.append(1)
                the_score = calculate_score_dealer(hand, score)
                print(hand)
                print(the_score)
            else:
                game_over = True
                break

        if the_score < 17 and the_score <= score:
            hand.append(draw())
            print(hand)
            # score = calculate_score_player(hand)
        else:
            end_turn = True
            break

        the_score = calculate_score_dealer(hand, score)
        print(the_score)

    if game_over:
        print(f"{name} has busted")
    return the_score


def compare(score_player, score_dealer):
    if score_player < score_dealer <= 21:
        print("Dealer has won the game")
    elif score_player == score_dealer:
        print("Result is a draw")
    else:
        print("Player wins the match")


hand_player = []
player_score = 0
player_hand_name = "Player hand"
hand_dealer = []
dealer_hand_name = "Dealer hand"
dealer_score = 0

hand_player.append(draw())
hand_player.append(draw())
print(hand_player)
player_score = calculate_score_player(hand_player)
print(f"Your current score is {player_score}\n")

hand_dealer.append(draw())
dealer_score = calculate_score_dealer(hand_dealer, player_score)
hand_dealer.append(draw())
print(f"The dealer's current score is {dealer_score}\n")

if player_score == 21:
    if dealer_score == 11:
        dealer_score = play_dealer(hand_dealer, player_score, dealer_hand_name)
        if player_score == dealer_score:
            print("Result is a draw")
        else:
            print(f"{player_hand_name} wins the match")
    else:
        print("You hit the blackjack, you win")

else:
    print("Would you like to split your hand, draw another card or end your turn")
    draw_or_split = input("Enter split for splitting, draw for drawing or end for ending your turn: ").lower()

    if draw_or_split == "split":
        hand_player_2 = []
        player_hand_name_2 = "2nd player hand"

        new_hand = hand_player.pop()
        player_score = calculate_score_player(hand_player)

        hand_player_2.append(new_hand)
        player_score_2 = calculate_score_player(hand_player_2)

        player_score = play(hand_player, player_hand_name)
        player_score_2 = play(hand_player_2, player_hand_name_2)

        if player_score <= 21 and player_score_2 <= 21:
            if player_score < player_score_2:
                dealer_score = play_dealer(hand_dealer, player_score_2, dealer_hand_name)
                compare(player_score_2, dealer_score)
            elif player_score > player_score_2:
                dealer_score = play_dealer(hand_dealer, player_score, dealer_hand_name)
                compare(player_score, dealer_score)
        elif player_score <= 21 < player_score_2:
            dealer_score = play_dealer(hand_dealer, player_score, dealer_hand_name)
            compare(player_score, dealer_score)
        elif player_score_2 <= 21 < player_score:
            dealer_score = play_dealer(hand_dealer, player_score_2, dealer_hand_name)
            compare(player_score_2, dealer_score)

    elif draw_or_split == "end":
        print(player_score)

        if player_score <= 21:
            dealer_score = play_dealer(hand_dealer, player_score, dealer_hand_name)
            compare(player_score, dealer_score)
    else:
        player_score = play(hand_player, player_hand_name)

        if player_score <= 21:
            dealer_score = play_dealer(hand_dealer, player_score, dealer_hand_name)
            compare(player_score, dealer_score)
