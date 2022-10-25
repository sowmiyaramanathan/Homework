import random                         # importing random to roll dice
import numpy as np                    # importing numpy to create a matrix
from tkinter import *                 # importing tinker to display the result as GUI
import tkinter.messagebox             # from tkinter importing messagebox to display result in a pop up
import re                             # importing re to display the board without square brackets

startNumber = 1                         # start number for rolling dice starting from 1               
endNumber = 6                           # end number for rolling dice till 6 only
opponentPlayer = None
playerOnePoint = 0                      # initializing player 1's point as 0
playerTwoPoint = 0                      # initializing player 1's point as 0
playTurn = 1                            # initializing the player's play as 1 to start with
root = Tk()

def createBoard():                      # function to create a 6x6 board
    global board                        # declaring board as global to access it in the program
    board = np.array([["PX", "PX", "PX", "PX", "PX", "PX"],
                      ["PX", "PX", "PX", "PX", "PX", "PX"],
                      ["PX", "PX", "PX", "PX", "PX", "PX"],
                      ["PX", "PX", "PX", "PX", "PX", "PX"],
                      ["PX", "PX", "PX", "PX", "PX", "PX"],
                      ["PX", "PX", "PX", "PX", "PX", "PX"]])        # creating a board as matrix

def rollDice(player):                                                     # function to roll dice
    diceRollRow = random.randint(startNumber, endNumber)            # getting a random number as row
    diceRollColumn = random.randint(startNumber, endNumber)         # getting a random number as column
    print(player, " rolled ", [diceRollRow,diceRollColumn])
    return [diceRollRow - 1,diceRollColumn - 1]                     # returning the row and column as a list

def choosePlayer(playTurn):                         # function to choose the current player and the opponent
    global opponentPlayer                           # declaring opponentPlayer as global to modify it here
    if playTurn % 2 != 0:                           # when the turn is odd
        opponentPlayer = "P2"                       # player 2 is the opponent
        return "P1"                                 # returning player 1
    else:                                           # when the turn is not odd
        opponentPlayer = "P1"                       # player 1 is the opponent
        return "P2"                                 # returning player 2

def checkWithInOne(matrix, position, opponentPlayer):   # function to see whether the spot claimed by the player has occupied by the opponent
    opponentPlayerPoint = 0                             # initializing opponent player's point as 0
    spotPresent = False                                     # initializing a variable that tracks the presence of opponents spots in the surrounding of claimed spot
    for row in range(-1, 2):                            # loop to change the row
        for column in range(-1, 2):                     # loop to change the column
            rangeOfRow = range(0, board.shape[0])       # finding row range
            rangeOfColumn = range(0, board.shape[1])    # finding column range
            (checkSpotRow, checkSpotColumn) = (position[0] + row, position[1] + column)  # finding the spot by adding the row and column position with the position of the claimed spot
            if (checkSpotRow in rangeOfRow) and (checkSpotColumn in rangeOfColumn) and (row, column) != (0, 0):    # when the checking spot is in the range and the spot is not the claimed spot
                if board[checkSpotRow, checkSpotColumn] == opponentPlayer:  #when the checking spot is occupied by the opponent
                    opponentPlayerPoint += 1            # increasing the opponent's point by 1; since the requirement does not mention how many times should the point of the opponent be increased in case he/she has occupied more than one spot around the current claimed spot, I'm increasing it for the number of spots he/she has occupied around the current player's claimed spot
                    spotPresent = True                      # declaring the spotPresent as true
    if spotPresent:                                         # when spotPresent is true
        return opponentPlayerPoint                          # returning opponent player's point
    else:                                                   # otherwise
        return 0                                            # returning 0

def checkSpots(diceNumber, currentPlayer, opponentPlayer):     # function to check the claimed spot
    currentPlayerPoint = 0                                     # initializing current players point as 0
    if board[diceNumber[0], diceNumber[1]] == opponentPlayer:  # checking if the claimed spot is occupied by the opponent
        currentPlayerPoint += 1                  # if the condition evaluates to true, player 1 gets one point
        board[diceNumber[0], diceNumber[1]] = currentPlayer     # assigning the claimed spot to player 1
        return [currentPlayer, currentPlayerPoint]              # returning the current player's name and points since the claimed spot is not occupied by the opponent the player who rolled the dice has raised score
    else:                                                # when the claimed spot is not occupies by player 1
            board[diceNumber[0], diceNumber[1]] = currentPlayer     # assigning the claimed spot to player 1
            opponentPlayerPoint = checkWithInOne(board, diceNumber, opponentPlayer) # calling checkWithInOne() to check spots claimed by the opponent with in one row or column
            return [opponentPlayer, opponentPlayerPoint]            # returning the opponent player's name and points since the claimed spot is not occupied by the opponent the opponent may raise score by the being in the surrounding spots
    
def declareResults(playerDetails):                              # function to decide who has won the game
    global playerOnePoint, playerTwoPoint                       # declaring the players points as global to modify them in this function
    print(re.sub('( \[|\[|\])', '', str(board)),)               # printing the board after the players has played and claimed their spot
    # increasing the respective player's points based on who scored points during the current turn
    if playerDetails[0] == "P1":
        playerOnePoint += playerDetails[1]                               # increasing player 1's points
        print("Player 1 has scored : ", playerOnePoint)                  # printing player 2's points
        if playerOnePoint == 5:                                          # when player 1 has scored 5 points
            tkinter.messagebox.showinfo("Game Over", "Player 1 has won") # printing player 1 has won
            exit()                                                       # game ends
    if playerDetails[0] == "P2":
        playerTwoPoint += playerDetails[1]                               # increasing player 2's points
        print("Player 2 has scored : ", playerTwoPoint)                  # printing player 2's points
        if playerTwoPoint == 5:                                          # when player 2 has scored 5 points
            tkinter.messagebox.showinfo("Game Over", "Player 2 has won") # printing player 1 has won
            exit()                                                       # game ends

print("\t\t\tGAME ROLLS")
createBoard()                                       # calling createBoard() to create a board
while True:                                         # players start to play the game
    playerName = choosePlayer(playTurn)         # calling choosePlayer() to get who is playing now
    diceNumber = rollDice(playerName)     # calling the rollDice() to roll the dice and storing the value in diceNumber
    playerDetails = checkSpots(diceNumber, playerName, opponentPlayer) # calling the checkSpots() to check spots
    declareResults(playerDetails)           # calling declareResults() to find whether the either one has scored five points
    playTurn += 1                             # increasing player turns to let the other player play the game




"""
                        GAME ROLLS
P1  rolled  [6, 2]
'PX' 'PX' 'PX' 'PX' 'PX' 'PX'
'PX' 'PX' 'PX' 'PX' 'PX' 'PX'
'PX' 'PX' 'PX' 'PX' 'PX' 'PX'
'PX' 'PX' 'PX' 'PX' 'PX' 'PX'
'PX' 'PX' 'PX' 'PX' 'PX' 'PX'
'PX' 'P1' 'PX' 'PX' 'PX' 'PX'
Player 2 has scored :  0
P2  rolled  [5, 4]
'PX' 'PX' 'PX' 'PX' 'PX' 'PX'
'PX' 'PX' 'PX' 'PX' 'PX' 'PX'
'PX' 'PX' 'PX' 'PX' 'PX' 'PX'
'PX' 'PX' 'PX' 'PX' 'PX' 'PX'
'PX' 'PX' 'PX' 'P2' 'PX' 'PX'
'PX' 'P1' 'PX' 'PX' 'PX' 'PX'
Player 1 has scored :  0
P1  rolled  [6, 4]
'PX' 'PX' 'PX' 'PX' 'PX' 'PX'
'PX' 'PX' 'PX' 'PX' 'PX' 'PX'
'PX' 'PX' 'PX' 'PX' 'PX' 'PX'
'PX' 'PX' 'PX' 'PX' 'PX' 'PX'
'PX' 'PX' 'PX' 'P2' 'PX' 'PX'
'PX' 'P1' 'PX' 'P1' 'PX' 'PX'
Player 2 has scored :  1
P2  rolled  [4, 1]
'PX' 'PX' 'PX' 'PX' 'PX' 'PX'
'PX' 'PX' 'PX' 'PX' 'PX' 'PX'
'PX' 'PX' 'PX' 'PX' 'PX' 'PX'
'P2' 'PX' 'PX' 'PX' 'PX' 'PX'
'PX' 'PX' 'PX' 'P2' 'PX' 'PX'
'PX' 'P1' 'PX' 'P1' 'PX' 'PX'
Player 1 has scored :  0
P1  rolled  [5, 5]
'PX' 'PX' 'PX' 'PX' 'PX' 'PX'
'PX' 'PX' 'PX' 'PX' 'PX' 'PX'
'PX' 'PX' 'PX' 'PX' 'PX' 'PX'
'P2' 'PX' 'PX' 'PX' 'PX' 'PX'
'PX' 'PX' 'PX' 'P2' 'P1' 'PX'
'PX' 'P1' 'PX' 'P1' 'PX' 'PX'
Player 2 has scored :  2
P2  rolled  [4, 6]
'PX' 'PX' 'PX' 'PX' 'PX' 'PX'
'PX' 'PX' 'PX' 'PX' 'PX' 'PX'
'PX' 'PX' 'PX' 'PX' 'PX' 'PX'
'P2' 'PX' 'PX' 'PX' 'PX' 'P2'
'PX' 'PX' 'PX' 'P2' 'P1' 'PX'
'PX' 'P1' 'PX' 'P1' 'PX' 'PX'
Player 1 has scored :  1
P1  rolled  [2, 2]
'PX' 'PX' 'PX' 'PX' 'PX' 'PX'
'PX' 'P1' 'PX' 'PX' 'PX' 'PX'
'PX' 'PX' 'PX' 'PX' 'PX' 'PX'
'P2' 'PX' 'PX' 'PX' 'PX' 'P2'
'PX' 'PX' 'PX' 'P2' 'P1' 'PX'
'PX' 'P1' 'PX' 'P1' 'PX' 'PX'
Player 2 has scored :  2
P2  rolled  [6, 5]
'PX' 'PX' 'PX' 'PX' 'PX' 'PX'
'PX' 'P1' 'PX' 'PX' 'PX' 'PX'
'PX' 'PX' 'PX' 'PX' 'PX' 'PX'
'P2' 'PX' 'PX' 'PX' 'PX' 'P2'
'PX' 'PX' 'PX' 'P2' 'P1' 'PX'
'PX' 'P1' 'PX' 'P1' 'P2' 'PX'
Player 1 has scored :  3
P1  rolled  [1, 6]
'PX' 'PX' 'PX' 'PX' 'PX' 'P1'
'PX' 'P1' 'PX' 'PX' 'PX' 'PX'
'PX' 'PX' 'PX' 'PX' 'PX' 'PX'
'P2' 'PX' 'PX' 'PX' 'PX' 'P2'
'PX' 'PX' 'PX' 'P2' 'P1' 'PX'
'PX' 'P1' 'PX' 'P1' 'P2' 'PX'
Player 2 has scored :  2
P2  rolled  [5, 4]
'PX' 'PX' 'PX' 'PX' 'PX' 'P1'
'PX' 'P1' 'PX' 'PX' 'PX' 'PX'
'PX' 'PX' 'PX' 'PX' 'PX' 'PX'
'P2' 'PX' 'PX' 'PX' 'PX' 'P2'
'PX' 'PX' 'PX' 'P2' 'P1' 'PX'
'PX' 'P1' 'PX' 'P1' 'P2' 'PX'
Player 1 has scored :  5

Player 1 has won
"""