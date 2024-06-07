
import random
from collections import Counter

#Asking to user to enter their name
name = input("What is your name? ")
print("Good Luck ", name, "\n\nLets play Hangman! Guess a character: ")

#Lists the possible words to be selected
words = ['rainbow', 'computer', 'science']
word = random.choice(words)

#If loop?

playing = True
letterguessed = ' '
chances = len(word) + 2
correct = 0
flag = 0


#Asks the user to input a guess
print("Guess a character")
guesses = ' '

##Want to add a section which selects the limit being the word length + 2
# Limits number of turns
turns = 12

#While loop checks if the user has guesses
while turns > 0:

    #Counting number of fails
    failed = 0

    for char in word:

        #Double check - but compares the selected word characters with the character guessed
        if char in guesses:
            print(char, end=" ")

        else:
            print("_")

            #Add a failed to the total
            failed += 1

    #Checks if failed is 0, if it is will print 'You win'
    if failed == 0:

        print("You win")
        #Prints the correct word
        print("The word is: ", word)
        break

    #If the wrong character will ask for another guess
    print()
    guess = input("Guess a character:")

    #Every input is stored in 'guesses'
    guesses += guess

    #Checks the guessed character
    if guess not in word:

        turns -= 1
        
        #If it isn't in the word will print 'Wrong'
        print("Wrong")
        #Will then print the number of guesses left
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You loose")

