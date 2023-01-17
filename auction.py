from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

#defining variable to end game and an empty dictionary
end_auction = False
bids = {}

#creating the fuction that loops through the dictionary
def auction(bid_auction):
  highest_bid = 0
  winner = ""
  for bidder in bid_auction:
    bid_amount = bid_auction[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner}, with bid of ${highest_bid}")

#creating a loop that allow multiple bidder until there are no more
while not end_auction:
  name = input("What is your name? \n").lower()
  bid = int(input("Enter a bid amount: \n$"))
  bids[name] = bid
  should_continue = input("Are ther still other bidders? \n").lower()
  if should_continue == "no":
    end_auction = True
    auction(bids)
    This is a replit clear fuction that disallow bidders see what others has bidded
  elif should_continue == "yes":
    clear()
