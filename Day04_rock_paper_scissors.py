rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
def print_choice(choice):
  if choice == 0:
    print(rock)
  if choice == 1:
    print(paper)
  if choice == 2:
    print(scissors)
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print_choice(user)

computer = random.randint(0, 2)
print(f"Computer chose {computer}")
print_choice(computer)

if computer == user:
  print("It's a draw!")
elif computer > user or (computer == 0 and user == 2):
  print("You lose!")
else:
  print("You Win!")