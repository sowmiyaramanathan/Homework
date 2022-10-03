import turtle                       #importing turtle package using which we can draw shapes in a canvas

def drawSquare(width):              #function to draw a square
    drawShape = turtle.Turtle()     #calling the constructor of the class Turtle() and keeping the instance reference
    sides = 4                       #initializing sides to 4 as the reference should draw 4 sides of the square
    for side in range(sides):       #running loop for the sides of square
        drawShape.forward(width)    #drawing a line forward
        drawShape.left(90)          #turning the cursor or pen pointer to 90 degree
    turtle.done()                   #closing the turtle

widthOfSquare = int(input("Enter the width of the square : "))      #reading the width of the square
if widthOfSquare <= 0:                              #checking whether the user has entered a values less than 0
    print("Enter width value above 0")              #displays the user to enter value above 0
else:                                               #otherwise
    drawSquare(widthOfSquare)                       #calling the function drawSqaure()