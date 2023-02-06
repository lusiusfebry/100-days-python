import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("Welcome to The Rock, Paper, Scissor Game")
userChoice = int(input("What do you choice? Type 0 for Rock, 1 for Paper or 2 for scissors\n"))
computerChoice = random.randint(0, 2)
gameImages = [rock, paper, scissors]
gameChoice = ["rock", "Paper", "Scissors"]

print(f"You choice {gameChoice[userChoice]}")
print(gameImages[userChoice])
print(f"Compurer choice {gameChoice[computerChoice]}")
print(gameImages[computerChoice])

if 3 < userChoice < 1:
    print("You choice wrong number")
elif userChoice == 2 and computerChoice == 0:
    print("You Lose")
elif userChoice == 0 and computerChoice == 2:
    print("You win")
elif computerChoice > userChoice:
    print("You Lose")
elif computerChoice < userChoice:
    print("You Win")
elif computerChoice == userChoice:
    print("It's a draw")
