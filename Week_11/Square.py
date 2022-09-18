def drawSquare(width):
    for side in range(width):
        for side2 in range(width):
            if side == 0 or side2 == 0 or side2 == width-1 or side == width-1:
                print("* ", end = "")
            else:
                print("  ", end = "")
        print("")

widthOfSquare = int(input("Enter the width of the square : "))
if widthOfSquare <= 0:
    print("Enter width above 0")
else:
    drawSquare(widthOfSquare)



"""
test case 1
Enter the width of the square : 10
* * * * * * * * * * 
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 * 
* * * * * * * * * *
________________________________________

test case 2
Enter the width of the square : 3
* * * 
*   * 
* * *
________________________________________

test case 3
Enter the width of the square : 5
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
________________________________________

test case 4
Enter the width of the square : 9
* * * * * * * * * 
*               * 
*               * 
*               * 
*               * 
*               *
*               * 
*               * 
* * * * * * * * *
________________________________________

test case 5
Enter the width of the square : -10
Enter above 0
"""