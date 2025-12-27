import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards=[]
computer_cards=[]

def deal_cards():
    for i in range(0, 2):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
    print(user_cards)
    print(computer_cards)


def calculate_score():
    for i in user_cards:
        


    if 11 or 10 in user_cards:
        print("User has a blackjack")

deal_cards()




