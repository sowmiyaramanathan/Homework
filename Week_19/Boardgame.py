import random                           #importing random to roll dice
import numpy as np                      #importing numpy to create a matrix

startNumber = 1                       #start number for rolling dice starting from 1                                     
endNumber = 6                           #end number for rolling dice till 6 only
playerOnePoint = 0                      #initializing player 1's point as 0
playerTwoPoint = 0                      #initializing player 1's point as 0
playTurn = 1                            #initializing the player's play as 1 to start with
# userWins = False                        #initializing user winning as false since the game has just started

def createBoard():                      #function to create a 6x6 board
    global board                        #declaring board as global to access it in the program
    board = np.array([["PX", "PX", "PX", "PX", "PX", "PX"],
                      ["PX", "PX", "PX", "PX", "PX", "PX"],
                      ["PX", "PX", "PX", "PX", "PX", "PX"],
                      ["PX", "PX", "PX", "PX", "PX", "PX"],
                      ["PX", "PX", "PX", "PX", "PX", "PX"],
                      ["PX", "PX", "PX", "PX", "PX", "PX"]])        #creating a board as matrix

def rollDice():                         #function to roll dice
    diceRollRow = random.randint(startNumber, endNumber)            #getting a random number as row
    diceRollColumn = random.randint(startNumber, endNumber)         #getting a random number as column
    return [diceRollRow,diceRollColumn]                             #returning the row and column as a list

def calculatePoint(diceNumber, playerTurn):                      #function to check the spot and assign points
    global playerOnePoint, playerTwoPoint      #declaring player points as global to use it throughout the code
    if playerTurn % 2 != 0:                                      #condition to check if it is player 1 turn
        if board[diceNumber[0]-1, diceNumber[1]-1] == "P2":      #condition to check claimed spot has occupied by player 2
            playerOnePoint += 1                                  #if the condition evaluates to true, player 1 gets one point
            board[diceNumber[0]-1, diceNumber[1]-1] = "P1"       #assigning the claimed spot to player 1
            print("Player One: ", playerOnePoint)                #printing player 1's point
        else:                                                    #when the claimed spot is not occupies by player 2
            board[diceNumber[0]-1, diceNumber[1]-1] = "P1"       #simply assigning the spot to player 1
    if playerTurn % 2 == 0:                                      #condition to check if it is player 2 turn
        if board[diceNumber[0]-1, diceNumber[1]-1] == "P1":      #condition to check whether the row and column spot has occupied by player 1
            playerTwoPoint += 1                                  #if the condition evaluates to true, player 2 gets one point
            board[diceNumber[0]-1, diceNumber[1]-1] = "P2"       #assigning the claimed spot to player 2
            print("Player Two : ", playerTwoPoint)               #printing player 2's point
        else:                                                    #when the claimed spot is not occupies by player 1
            board[diceNumber[0]-1, diceNumber[1]-1] = "P2"       #simply assigning the spot to player 2

def declareResults():                                               #function to decide who has won the game
    if playerOnePoint == 5:                                         #when player 1 has scored 5 points
        print("Player 1 has won")                                   #printing player 1 has won
        exit()                                                      #game ends
    if playerTwoPoint == 5:                                         #when player 2 has scored 5 points
        print("Player 2 has won")                                   #printing player 1 has won
        exit()                                                      #game ends

createBoard()                                       #calling createBoard() to create a board
while True:                                         #players start to play the game
    diceNumber = rollDice()     #calling the rollDice() to roll the dice and storing the value in diceNumber
    calculatePoint(diceNumber, playTurn)      #calling the calculatePoint() to check spots and increase points
    playTurn += 1                             #increasing player turns to let the other player play the game
    declareResults()            #calling declareResults() to find whether the either one has scored five points