#Imports
import random
import math

#Inputs
lower = int(input("Enter Lower Bound Limit:- "))
upper = int(input("Enter Upper Bound Limit"))

#Number Gen
x = random.randint(lower, upper)
print("\n\tYou've only "
      round(math.log(upper - lower + 1, 2)),
      " Chances to guess the integer!\n")

#No of Guesses
count = 0

#For Calc
while count < math.log(upper - lower +1, 2):
    count += 1

    #Input for Guess
    guess = int(input("Guess a number:- "))

    #Condition Loop
    if x == guess:
        print("Correct! Well done :)",
              count, " try")
        #If Correct Loop Breaks
        break
    elif x > guess:
        print("Wrong... Too small")
    elif x < guess:
        print("Wrong... Too big")

if count >= math.log(upper - lower + 1, 2):
    print("znThe number is %d" % x)
    print("\tBetter Luck Next Time!")
