# blind bidding
from art import logo

print(logo)

bidders = []

def make_a_bid(bidder):
    bid_continues = True
    while bid_continues:
        name = str(input("Enter your name: "))
        bid = float(input("Enter how much you bid: "))
        bidder.append({"name": name, "bid": bid})
        yes_or_no = str(input("Are there any other bidders, yes or no: ")).lower()
        if yes_or_no == "no":
            bid_continues = False

    highest = 0
    highest_bidder = ""
    for bid in bidder:
        if bid["bid"] > highest:
            highest = bid["bid"]
            highest_bidder = bid["name"]
    print(f"Highest bidder is {highest_bidder} with ${highest} as their offer")

make_a_bid(bidders)