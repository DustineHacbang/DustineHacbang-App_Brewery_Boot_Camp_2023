from replit import clear
#HINT: You can call clear() to clear the output in the console.
adding_more_biders = True
bids = {}

def find_highest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_total = bidding_record[bidder]
        if bid_total > highest_bid:
            highest_bid = bid_total
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while  adding_more_biders == True:
    
    name = input("What is your name?:")
    amount = int(input("What is your bid?:"))
    bids[name] = amount
    continue_bidding = input("Are there anyother bidders? Type 'Yes' or 'No'.\n")
    
    if continue_bidding == "no":
        adding_more_biders = False
        find_highest_bid(bids)
    elif adding_more_biders =="yes":
        clear()
    