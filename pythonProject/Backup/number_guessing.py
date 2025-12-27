import random
from number_guess_logo_art import *
print(logo)
print("Welcome to the Number Guessing Game!!\n")
print("I'm thinking of a number between 1 and 100")
computer_choice = random.randint(1, 100)
print(computer_choice)
level = input("Choose a difficulty. Type 'easy' or 'hard': ")

def calculation(level):
    if level == 'easy':
        attempt_count = 10
    else:
        attempt_count = 5
    for i in range(1,attempt_count):
        print(f"You have {attempt_count} attempts remaining to guess the number")
        user_guess = int(input(f"Make a guess!\n"))
        if user_guess > computer_choice:
            print("Too High")
        elif user_guess == computer_choice:
           return print(f"Correct! the value is {computer_choice}")
        else:
            print("Very low")
        attempt_count -= 1


calculation(level)