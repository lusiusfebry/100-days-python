from art import logo
import random

HARD_LEVEL = 5
EASY_LEVEL = 10


def randomNumber():
    return random.randint(1, 100)


def checkAnswer(guess, answer, turn):
    if guess > answer:
        print("Too High")
        return turn - 1
    elif guess < answer:
        print("Too Low")
        return turn - 1
    else:
        print(f"you got it, the answer is {answer}")

def diffilcuty():
    diffilcuty = input("Choose a difficulty. Type \'easy\' or \'hard\': ").lower()
    if diffilcuty == "easy":
        return EASY_LEVEL
    return HARD_LEVEL

def main():
    print(logo)

    print("Welcome to The Number Guessing Games")
    print("I'm thinking of the number between 1 and 100")
    number = randomNumber()
    print(f"psst, the correct number is {number}")
    turn = diffilcuty()

    guess = 0

    while guess != number:
        print (f"You have {turn} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        turn = checkAnswer(guess,number,turn)

        if turn == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != number:
            print("Guess again.")




main()
