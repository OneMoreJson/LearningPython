# Set Up
#   1. Board consists of 9 squares (1-9)
#   2. Player chooses a square between 1 and 9 (inclusively)
#   3. If square is taken, player is asked to choose again
#   4. If player gets three squares in a row, player wins
#   5. If all squares are taken and no player has three in a row,
#      a tie is declared and the player is asked if they want to play
#      again
#   6. The opponent is computer.  Computer will choose randomly
#      between 1-9 (minus squares taken)
#   7. Win or loose, player is asked if they want to play again
#   8. Board Set-Up:
#
#        |       |
#    1   |   2   |   3
# _______|_______|_______
#        |       |
#    4   |   5   |   6
# _______|_______|_______
#        |       |
#    7   |   8   |   9
#        |       |
#


# IMPORTS
import random

# VARS
places = [1, 2, 3, 4, 5, 6, 7, 8, 9]
playerChoices = []
compChoices = []
play = True
win = False

# Start Function


# Instructions
def inst():
    print('Welcome to Py Tick Tack Toe')
    print('')
    print('You will be "X" while your opponent will be "O"')
    print('')
    print('You will take turns selecting squares')
    print('If you get three squares in a row, you win!')


# Build Board
def bb():

    print('       |       |')
    print('   {}   |   {}   |   {}' .format(places[0], places[1], places[2]))
    print('_______|_______|_______')
    print('       |       |')
    print('   {}   |   {}   |   {}' .format(places[3], places[4], places[5]))
    print('_______|_______|_______')
    print('       |       |')
    print('   {}   |   {}   |   {}' .format(places[6], places[7], places[8]))
    print('       |       |')


# Check Valid Choice
def selectionCheck(choice, places):

    if(choice in places):
        return True
    else:
        return False


# Computer Choice
def compChoice():
    out = random.randint(1, 9)

    if(selectionCheck(out, places)):
        return out
    else:
        return compChoice()


# Player Choice
def playerChoice():
    try:
        selection = int(input(
            'Please select a number square that has not been taken\n'))
    except ValueError:
        print('That was not a number...')
        return playerChoice()

    if(selectionCheck(selection, places)):
        return selection
    else:
        print("I'm sorry, that is an invalid input.")
        return playerChoice()
