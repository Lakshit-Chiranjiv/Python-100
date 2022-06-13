print("Welcome to Blind Auction")
bids = {}
auction_live = True
highest_bid = 0
highest_bidder = ''
while auction_live:
    name = input("Enter your name : ")
    bidPrice = int(input("Enter your bid : $"))
    if bidPrice > highest_bid:
        highest_bid = bidPrice
        highest_bidder = name
    bids[name] = bidPrice
    choice = input("Does anyone else would like to make a bid - YES / NO : ")
    auction_live = choice == "YES"

print("The auction is over")
print(f"{highest_bidder} wins the auction item with a bid of ${highest_bid}")

print("The bid list goes as follows : ")
print("Bidder \t Bid")
for i in bids:
    print(f"{i} \t {bids[i]}")

print("\nThankyou for joining our auction")