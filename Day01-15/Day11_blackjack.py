############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from functions import clear
from ascii_art import blackjack_logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def find_winner(player_cards, computer_cards):
    player = sum(player_cards)
    dealer = sum(computer_cards)
    if dealer == 21:
        print("Dealer has blackjack!  You lose!")
    elif player == 21:
        print("You have blackjack!  You Win!")
    elif player > 21:
        print(f"You scored {player}. You lose!")
    elif dealer > 21:
        print(f"Dealer scored {dealer}. You win!")
    elif dealer == player:
        print("It is a draw!")
    elif (21 - dealer) < (21 - player):
        print("You lose")
    else:
        print("You win!")

def eleven_to_one(hand):
    ace = hand.index(11)
    hand[ace] = 1
    return hand

def deal_card():
    card = random.choice(cards)
    return card

def play():
    clear()
    game_over = False
    # Create lists for hands
    player_cards = []
    computer_cards = []
    print(blackjack_logo)

    # Deal two cards to each
    for i in range(0, 2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())
    if sum(computer_cards) < 17:
        computer_cards.append(deal_card())

    print(f"Your cards are {player_cards} score {sum(player_cards)}")
    print(f"computers first card is {computer_cards[0]}")

    while not game_over:
        if sum(player_cards) > 21:
            if 11 in player_cards:
                player_cards = eleven_to_one(player_cards)
            else:
                game_over = True

        if sum(player_cards) == 21:
            game_over = True

        if sum(player_cards) < 21:
            deal = input("Do you want another card?")
            if deal == "y":
                player_cards.append(deal_card())
                print(f"Your cards are {player_cards} score {sum(player_cards)}")
            else:
                game_over = True
    if sum(computer_cards) > 21 and 11 in computer_cards:
        computer_cards = eleven_to_one(computer_cards)
    print(f"Computer's cards are {computer_cards} score {sum(computer_cards)}")
    find_winner(player_cards, computer_cards)

    play_again = input("Play again? y or n ")
    if play_again == "y":
        play()

play()
