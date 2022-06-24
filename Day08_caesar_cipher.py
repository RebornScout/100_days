alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from Day08_caesar_art import logo


print(logo)
def caesar(text, shift, direction):
    result = ""
    if direction == "decode":
        shift = -shift
    for letter in text:
        try:
            letter_index = alphabet.index(letter)

            if letter_index + shift > 25:
                result += alphabet[letter_index + shift - 26]
            else:
                result += alphabet[letter_index + shift]
        except ValueError:
            result += letter
    print(f"The result is {result}")

go_again = True
while go_again == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    restart = input("Type 'yes' to go again or 'no' to quit.")
    if restart == "no":
        go_again == False
