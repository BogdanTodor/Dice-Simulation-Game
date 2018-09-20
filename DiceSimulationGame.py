from random import *

def diceRoll():
    global rollValue
    rollValue = randint(1,6)
    print(rollValue)

def program():
    numrolls = 0
    userInput = 'y'
    global rollValue
    score = 0
    while userInput != 'n' or userInput != 'N':
        print('Would you like to roll the dice?')
        userInput = input('y/n?')
        if userInput =='y' or userInput =='Y':
            numrolls = numrolls + 1
            diceRoll()
            score = score + rollValue
        else:
            print('You rolled', numrolls, ' dice')
            print('Your score is: ', score)
            print('Thanks for playing, game over')
            break;

print("\nWelcome to dice roller pro!!!\n")
program()