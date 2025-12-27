import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#user_turn = input("press 'h' to hit and 's' to stand\n")
user_cards = []
computer_cards = []
def deal_card(user_cards, computer_cards):
    for i in range(0, 2):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
    return user_cards, computer_cards


def calculate_score(user_cards, computer_cards):
    user_score = 0
    computer_score = 0
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)
    if user_score == 21 and len(user_cards) ==2:
        print(" User has Black Jack")
    elif computer_score == 21 and len(computer_cards) ==2:
        print("Computer has Black Jack")
    else:
        if user_score > 21:
            if user_cards in 11
