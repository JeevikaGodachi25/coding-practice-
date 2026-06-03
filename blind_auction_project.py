# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo
print(logo)
bid_dictionary = {}
answer=True
def max_bid_dictionary(bid_dictionary):
    max_value=0
    key=""
    for i in bid_dictionary:
        if bid_dictionary[i]>max_value:
            max_value=bid_dictionary[i]
            key=i
    print(f"The winner is {key} with a bid of ${max_value}")
while answer:
        person1=input("Enter your name?:")
        person1_bid=int(input("Enter your bid? $"))
        print("\n"*100)
        bid_dictionary[person1]=person1_bid
        choice=input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        if choice=="no":
            max_bid_dictionary(bid_dictionary)
            answer=False
         