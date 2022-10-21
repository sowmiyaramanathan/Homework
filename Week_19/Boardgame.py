import random
import numpy as np

def createBoard():
    global board
    board = np.array([['X', 'X', 'X', 'X', 'X', 'X'],
                      ['X', 'X', 'X', 'X', 'X', 'X'],
                      ['X', 'X', 'X', 'X', 'X', 'X'],
                      ['X', 'X', 'X', 'X', 'X', 'X'],
                      ['X', 'X', 'X', 'X', 'X', 'X'],
                      ['X', 'X', 'X', 'X', 'X', 'X']])

def rollDice():
    diceRollRow = random.randint(startNumber, endNumber)
    diceRollColumn = random.randint(startNumber, endNumber)
    diceNumber = [diceRollRow, diceRollColumn]
    print(diceNumber)
    return [diceRollRow,diceRollColumn]

def checkPoint(diceNumber, playerTurn):
    print(diceNumber)
    global playerOnePoint, playerTwoPoint
    if playerTurn % 2 != 0:
        if board[diceNumber[0], diceNumber[1]] == "P2":
            playerOnePoint += 1
        else:
            board[diceNumber[0], diceNumber[1]] = "P1"
    if playerTurn % 2 == 0:
        if board[diceNumber[0], diceNumber[1]] == "P1":
            playerTwoPoint += 1
        else:
            board[diceNumber[0], diceNumber[1]] = "P2"
def declareResults():
    if playerOnePoint > 5:
        print("Player 1 has won")
        exit()
    if playerTwoPoint > 5:
        print("Player 2 has won")
        exit()

board = None
startNumber = 1
endNumber = 6
playerOnePoint = 0
playerTwoPoint = 0
playCount = 1
userWins = False

createBoard()
while userWins == False:
    print(board)
    diceNumber = rollDice
    userWins = checkPoint(diceNumber, playCount)
    declareResults()