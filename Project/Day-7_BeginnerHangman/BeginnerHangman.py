from HangmanArt import logo, stages
from HangmanWordlist import word_list
from random import choice
import os
print(logo)
randomWord = choice(word_list)
print(f"the word is {randomWord}")

# create empty list from random word list and add "_" to the list
display = []
for _ in randomWord:
    display += "_"

endOfGame = False
lives = 6

while not endOfGame:
    guess = input("Guess a letter : ").lower()

    # os.system('cls || clear')
    # print(chr(27) + "[2J")

    if guess in display:
        print(f"You have already guess {guess}")

    # check if guess letter is in the random word chosen, if is in the random, append those letter to the list
    for letter in range(len(randomWord)):
        if randomWord[letter] == guess:
            display[letter] = guess
            # endOfGame = True

    if guess not in randomWord:
        print(f"You guess {guess} not in chosen word. You have lost 1 lives")
        lives -= 1
        if lives == 0:
            endOfGame = True

    print(f"{' '.join(display)}")

    if "_" not in display:
        endOfGame = True
        print ("You win")
    print(stages[lives])
