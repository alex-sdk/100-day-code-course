from art import logo

print(logo)
bids = {}
bid_list = []
on_off = True

while on_off:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))

    bids[name] = bid

    other_bid = input("Are there any other bids? Type 'yes' or 'no'.\n" )

    if other_bid == 'no':
        on_off = False
        for bid_name in bids:
            bid_amount = bids[bid_name]
            bid_list.append(bid_amount)
        
        auction_win = max(bid_list)

        for key, value in bids.items():
            if auction_win == value:
                print(f"Congrats to {key} you have won the auction.")
                break