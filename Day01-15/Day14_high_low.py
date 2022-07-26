from functions import clear
from ascii_art import vs, high_low_logo
from Day14_data import data
import random

def compare_line(x):
    person = data[x]
    person_string = f"{person['name']}, a {person['description']}, from {person['country']}"
    return person_string

def update_question(a):
    compare_options = True
    while compare_options:
        b = random.randint(0, len(data))
        if b != a:
            compare_options = False
    return b

def check_answer(a, b, answer):
    person_a = data[a]["follower_count"]
    person_b = data[b]["follower_count"]
    if answer == "A" and person_a > person_b:
        return False
    elif answer == "B" and person_b > person_a:
        return False
    else:
        return True

def game_output(a, b, score):
    clear()
    print(high_low_logo)
    if score > 0:
        print("You're right! Current Score:", score)
    print("Compare A:", compare_line(a))
    print(vs)
    print("Against B:", compare_line(b))

def play():
    score = 0
    compare_a = random.randint(0, len(data))

    game_over = False
    while not game_over:
        compare_b = update_question(compare_a)
        game_output(compare_a, compare_b, score)

        answer = input("Who has more followers? Type 'A' or 'B' ").upper()
        game_over = check_answer(compare_a, compare_b, answer)
        if not game_over:
            score += 1
            compare_a = compare_b

    clear()
    print(high_low_logo)
    print("Bad luck that was the wrong answer!  You scored", score)
    play_again = input("Play again? Type y or n.").lower()
    if play_again == "y":
        play()




play()