from caesar_logo import *

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text,direction,shift):
    if shift > 52:
        shift %= 52
    final_word = ''
    for letter in text:
        if letter not in alphabet:
            final_word += letter
        else:
            number = alphabet.index(letter)
            if direction == 'encrypt':
                final_word += alphabet[number + shift]
            elif direction == 'decrypt':
                final_word += alphabet[number - shift]
            else:
                print("You have entered worng option")
    print(f'Your {direction}ed text is {final_word}')

user_entry = True
while user_entry == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text=text, direction=direction, shift=shift)
    user_text = input("Type yes to continue no to quit\n").lower()
    if user_text == 'no':
        user_entry = False
        print("Good Bye!")