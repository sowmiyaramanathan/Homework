from bookAPlane import *

class bookingDetails(bookAPlane):
    def printDetails(self):
        print(self.passengerName + self.arrivalPlace + self.departurePlace)