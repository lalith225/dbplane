from replit import clear

user_entry = True
bid_data = {}
while user_entry:
    user_name = input("What is your name?\n").lower()
    bid_value = int(input("What is your bid value?\n"))
    bid_data[user_name] = bid_value
    other_bidder = input("Is there any other bidder then type yes or no!\n")
    if other_bidder == 'yes':
        clear()
    else:
        greater_bid=0
        winner = ""
        for key in bid_data:
            if bid_data[key] >= greater_bid:
                greater_bid = bid_data[key]
                winner = key
        print(f'The highest bid is made by {winner} and bid value is {greater_bid}')
        user_entry = False