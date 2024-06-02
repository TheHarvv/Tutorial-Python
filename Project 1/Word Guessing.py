#Imports modules into Python
import random

#Asking to user to enter their name
name = input("What is your name?")
print("Good Luck ", name)

#Lists the possible words to be selected
words = ['rainbow', 'computer', 'science',
          'programming', 'python', 'mathematics',
            'player', 'condition', 'reverse',
              'water', 'board', 'geeks']

#Function chooses one random word
word = random.choice(words)

#Asks the user to input a guess
print("Guess a character")
guesses = ' '

# Limits number of turns
turns = 12

#While loop checks if the user has guesses
while turns > 0:

    failed = 0

    for char in word:

        if char in guesses:
            print(char, end=" ")

        else:
            print("_")
            failed += 1

    if failed == 0:

        print("You win")

        print("The word is: ", word)
        break

    print()
    guess = input("Guess a character:")

    #Every input is stored in 'guesses'
    guesses += guess

    if guess not in word:

        turns -= 1

        print("Wrong")

        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You loose")