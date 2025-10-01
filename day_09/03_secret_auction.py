from art import auction_logo, gavel

print(auction_logo)
print(gavel)
print(" Welcome to the Secret Auction")
print("Place your bids and see who wins!")
print("=" * 50)

def find_highest_bid(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f" The winner is {winner} with the highest bid of ₹{highest_bid}")

# Initialize dictionary and variables
bidders = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name: ")
    bid = int(input(" What is your bid: ₹"))
    bidders[name] = bid
    
    should_continue = input(" Any other bidder? Type 'yes' or 'no': ").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bid(bidders)

print("\n Thank you for participating in the auction")







