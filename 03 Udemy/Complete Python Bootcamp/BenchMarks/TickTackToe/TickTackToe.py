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
from IPython.display import clear_output

# VARS
places = [1, 2, 3, 4, 5, 6, 7, 8, 9]
playerChoices = []
compChoices = []
playerTurn = True
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
    print('\n\n')
    runGame(playerTurn)


# Continue?
def contGame():
    choice = input('Would you like to play again? (Yes or Now)').lower()

    if choice == 'yes' or choice == 'y':
        places = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        playerChoices = []
        ompChoices = []
        return runGame(playerTurn)
    elif choice == 'no' or choice == 'n':
        return endGame()
    else:
        print('That was an invalid answer...')
        return contGame()


# End Game
def endGame():
    print('Thank you for playing Py Tick Tack Toe!')


# Build Board
def bb():

    clear_output()

    print('       |       |')
    print('   {}   |   {}   |   {}' .format(places[0], places[1], places[2]))
    print('_______|_______|_______')
    print('       |       |')
    print('   {}   |   {}   |   {}' .format(places[3], places[4], places[5]))
    print('_______|_______|_______')
    print('       |       |')
    print('   {}   |   {}   |   {}' .format(places[6], places[7], places[8]))
    print('       |       |')
    print('\n')


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


# Replace Square number with X or O
def replaceSquare(xo, selection, places):
    for i in range(len(places)):
        if places[i] == selection:
            places[i] = xo
    bb()
    return places


# Winner?
def checkWinner(playerSelections, playerTurn, player):
    win1 = [1, 2, 3]
    win2 = [4, 5, 6]
    win3 = [7, 8, 9]
    win4 = [1, 4, 7]
    win5 = [2, 5, 8]
    win6 = [3, 6, 9]
    win7 = [1, 5, 9]
    win8 = [3, 5, 7]

    win1Check = all(elem in playerSelections for elem in win1)
    win2Check = all(elem in playerSelections for elem in win2)
    win3Check = all(elem in playerSelections for elem in win3)
    win4Check = all(elem in playerSelections for elem in win4)
    win5Check = all(elem in playerSelections for elem in win5)
    win6Check = all(elem in playerSelections for elem in win6)
    win7Check = all(elem in playerSelections for elem in win7)
    win8Check = all(elem in playerSelections for elem in win8)

    if win1Check or win2Check or win3Check or win4Check or win5Check or win6Check or win7Check or win8Check:
        print('{} Won!!!' .format(player))
    elif len(playerChoices) == 5:
        print('##############################\n')
        print("Game is a Draw!")
        contGame()
    else:
        playerTurn = not playerTurn
        runGame(playerTurn)


# Run Game (Start with player)
def runGame(playerTurn):

    if(playerTurn):
        # Player selects
        selection = playerChoice()
        # Store selection in player list
        playerChoices.append(selection)
        # Change Board list
        # Rewrite Board
        replaceSquare('X', selection, places)

        # Check if there is a win
        # change players
        checkWinner(playerChoices, playerTurn, 'You')

        print('\n')

    else:

        # Comp selects
        selection = compChoice()
        # Store selection in comp list``
        compChoices.append(selection)
        # Change Board list
        # Rewrite Board
        replaceSquare('O', selection, places)

        # Check if there is a win
        # change players
        checkWinner(compChoices, playerTurn, 'Computer')

        print('\n')
