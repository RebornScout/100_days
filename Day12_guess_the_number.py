from functions import clear
import random

def play():
    clear()
    number = random.randint(1, 101)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    level = input("Choose a difficulty. Type 'easy or 'hard': ")
    if level == "easy":
        guesses = 10
    else:
        guesses = 5

    game_over = False
    while not game_over:
        print(f"You have {guesses} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print("Well done! You guessed correctly!")
            game_over = True
        else:
            guesses -= 1
            if guess > number:
                print("Too high.")
            else:
                print("Too low")
            if guesses == 0:
                game_over = True
                print("You have run out of attempts.")
    print(number)
    play_again = input("Do you want to play again? Type 'y' or 'n'; ")
    if play_again == "y":
        play()

play()