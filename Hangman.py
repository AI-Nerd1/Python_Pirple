import random as r
# from nltk.corpus import words
import os


Hanging = [
    """
     ______
    |      |
    |
    |
    |
    |
    |
----------
""",
    """
     ______
    |      |
    |      O
    |
    |
    |
    |
----------
""",
    """
     ______
    |      |
    |      O
    |     /|
    |
    |
    |
----------
""",
    """
     ______
    |      |
    |      O
    |     /|\\
    |
    |
    |
----------
""",
    """
     ______
    |      |
    |      O
    |     /|\\
    |      |
    |
    |
----------
""",
    """
     ______
    |      |
    |      O
    |     /|\\
    |      |
    |     /
    |
----------
""",
    """
     ______
    |      |
    |      O
    |     /|\\
    |      |
    |     / \\
    |
----------
"""
]
Random_word = ""
Unknown_word = []
Known_word = []


def select(i):
    if i == 2:
        word_list = words.words()
        Random_word = r.choice(word_list)
    elif i == 1:
        Random_word = input("Enter the word: ")
    for i in range(len(Random_word)):
        Unknown_word.append("_")
        Known_word.append(Random_word[i].upper())

def letterArrayCheck(letter,Array = []):
    try:
        Array.index(letter.upper())
        return True
    except:
        return False



def playGame():
    inp = input("Press 1 to Start the game\n")
    select(int(inp))
    statusBool = None
    counter = 0
    pickLettersStr = ""
    pickLetters = []
    letterBool = False
    while True:
        stage = Hanging[counter]
        if statusBool == False:
            print("Wrong guess!")
        elif statusBool:
            print("You guessed right!")
        print(stage)
        for i in range(len(Unknown_word)):
            print(Unknown_word[i], end=" ")
        print("\nPicked letters: " + pickLettersStr, end="")
        letter = input("\nPlease guess a letter: ")
        letterBool = letterArrayCheck(letter, pickLetters)
        while letterBool:
            letter = input("You already picked that letter! Please pick another letter: ")
            letterBool = letterArrayCheck(letter, pickLetters)
        pickLettersStr += letter.upper() + ", "
        pickLetters.append(letter.upper())
        statusBool = guess(letter)
        if not statusBool:
            counter += 1
        if counter >= 6:
            print(chr(27) + "[2J")
            stage = Hanging[counter]
            print(stage)
            print("You lost the game! The word was: " + Random_word.upper())
            break
        else:
            if not letterArrayCheck("_", Unknown_word):
                print("You won!")
                break
        print(chr(27) + "[2J")


def guess(letter):
    counter = -1
    for i in range(len(Known_word)):
        if Known_word[i] == letter.upper():
            Unknown_word[i] = Known_word[i]
            counter += 1
    if counter > -1:
        return True
    else:
        return False

playGame()