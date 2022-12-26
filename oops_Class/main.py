from bookAPlane import *
from bookingDetails import *

def canStartBooking(canStart):
    # book = bookAplane()
    # book.getBookingDetails()
    book = bookingDetails()
    book.getBookingDetails()
    book.printDetails()

openToBook = int(input("Press 1 to start booking plane; else press any key    : "))

if openToBook == 1:
    canStartBooking(True)
else:
    exit()