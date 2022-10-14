from replit import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
item = ["Novelty Barware", "Hunting Decoys", "Depression Glass", "Original Paintings", "Postcards"]
import random
print("Welcome to the 𝕿𝖍𝖊 𝖘𝖊𝖈𝖗𝖊𝖙 𝖆𝖚𝖈𝖙𝖎𝖔𝖓")
print(logo)
item_auction = random.choice(item)
print(f"The item is: {item_auction}")
other_bidder = True
def highest(bidding_record):
  highest_bid = 0
  winner = ""
  for key in bidding_record:
    money = bidding_record[key]
    if money > highest_bid:
      highest_bid = money
      winner = key
  print(f"The item {item_auction} is sold to {winner}!")
  
bids = {}
while other_bidder:
  name = input("What is your name?")
  value = int(input("How much you bidding for?"))
  bids[name] = value
  an = input("Any other bidders?")
  if an == "yes":
     clear()
  elif an == "no":
    other_bidder =  False
    highest(bidding_record = bids)

