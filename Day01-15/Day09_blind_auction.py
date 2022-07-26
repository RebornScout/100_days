from functions import clear
from ascii_art import auction_logo

print(auction_logo)
auction_bids = {}

more_bids = True
while more_bids:
    name = input("What is your name?\n")
    bid = int(input("How much would you like to bid?\n£"))
    auction_bids[name] = bid
    new_bid = input("Are there any more bidders? y/n\n")
    if new_bid == "y":
        clear()
    else:
        more_bids = False

max_bid = 0
winner = ""

for bidder in auction_bids:
    if auction_bids[bidder] > max_bid:
        winner = bidder
        max_bid = auction_bids[bidder]

print(f"{winner} is the lot winner with a bid of £{max_bid}")
