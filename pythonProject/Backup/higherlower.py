import random

import higher_lower_logo
from higher_lower_data import *
from higher_lower_logo import *

print(higher_lower_logo.logo)
def get_data():
    a = data[random.randint(0, len(data) - 1)]
    b = data[random.randint(0, len(data) - 1)]

    if a['name'] == b['name']:
        a = data[random.randint(0, len(data) - 1)]
    return a , b
def serve_data():
    print(f'Compare A: {a['name']}, a {a['description']},from {a['country']}, {a['follower_count']}')
    print(higher_lower_logo.vs)
    print(f'Against B: {b['name']}, a {b['description']},from {b['country']}, {b['follower_count']}')

serve_data()
still_won = True
score = 0
while still_won == True:
    user_guess = input("Who has more followers? Type 'A' or Type 'B':\n").lower()
    if user_guess == 'a':
        if a['follower_count'] > b['follower_count']:
            print("You won")
            score += 1
            if score > 0:
                print(f'You score is {score}')
            serve_data()
        else:
            print("You lose")
            still_won = False
    if user_guess == 'b':
        if b['follower_count'] > a['follower_count']:
            print("You won")
            score += 1
            if score > 0:
                print(f'You score is {score}')
            serve_data()
        else:
            print("You lose")
            still_won = False



