import turtle

def drawSquare(width):
    drawShape = turtle.Turtle()
    sides = 4
    for side in range(sides):
        drawShape.forward(width)
        drawShape.left(90)
    turtle.done()

widthOfSquare = int(input("Enter the width of the square : "))
if widthOfSquare <= 0:
    print("Enter width value above 0")
else:
    drawSquare(widthOfSquare)