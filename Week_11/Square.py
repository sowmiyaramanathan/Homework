def drawSquare(width):              #function to draw a square
    for side in range(width):       #running loop for row / horizontal line
        for side2 in range(width):  #running loop for column / vertical
            if side == 0 or side2 == 0 or side2 == width-1 or side == width-1:  #when cursor is either at the first position on row or column or at the postion less than its side length
                print("* ", end = "")                                           #print '* '
            else:                                                               #at other positions
                print("  ", end = "")                                           #leaves space
        print("")                                                               #moving to next line

widthOfSquare = int(input("Enter the width of the square : "))      #reading the width of the square
if widthOfSquare <= 0:                              #checking whether the user has entered a values less than 0
    print("Enter width above 0")              #displays the user to enter value above 0
else:                                               #otherwise
    drawSquare(widthOfSquare)                       #calling the function drawSqaure()



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