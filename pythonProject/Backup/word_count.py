import random
import hangman_logo
import hangman_word_list
print(hangman_logo.logo)
#word_list = ["advark", "baboon", "camel"]
choosed_word = random.choice(hangman_word_list.word_list)
print(f"choosed word is {choosed_word}")
final_list = []
lives = 6
for letter in choosed_word:
    final_list += "_"
end_game = True
while end_game:
    user_guess = input("Guess the letter\n").lower()
    for i in range(len(choosed_word)):
        letter = choosed_word[i]
        if letter == user_guess:
            final_list[i] = letter
    print(final_list)
    if user_guess not in final_list:
        lives -= 1
        print(hangman_logo.stages[lives])
        if lives == 0:
            end_game = False
            print("You lose")
    else:
        print(hangman_logo.stages[lives])
    if "_" not in final_list:
        end_game = False
        print("You win")
