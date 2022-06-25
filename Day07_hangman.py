from random import choice
from time import sleep
from ascii_art import hangman_logo, hangman_lives
from functions import clear

# refresh the screen
def refresh():
    clear()
    print(answer)
    print(hangman_lives[lives])
    print(display)

# import words list
with open("words.txt") as words_file:
    words = words_file.read().split("\n")
    word_list = [word.strip('"').lower() for word in words if len(word) > 5]

# Clear display and show logo
clear()
print(hangman_logo)
sleep(3)

# Set game variables
answer = choice(word_list)
display = ['_' for letter in answer]
lives = 6
game_over = False
guesses = []

refresh()

while game_over != True:
    guess = input("Enter your guess: ").lower()
    if guess not in guesses:
        guesses.append(guess)
    else:
        print("You have already tried that letter!")
        sleep(2)
        continue
    for i in range(len(answer)):
        if guess == answer[i]:
            display[i] = guess
    if guess not in answer:
        lives -= 1
    refresh()

    if "_" not in display:
        print("You win!")
        game_over = True
    if lives == 0:
        print("You lose!")
        game_over = True