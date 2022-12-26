class passengerDetails():
    passengerName = ''
    arrivalPlace = ''
    departurePlace = ''

    def setPassengerName(self):
        self.passengerName = input("Enter passenger name : ")

    def setArrivalPlace(self):
        self.arrivalPlace = input("Enter arrival place : ")

    def setDeparturePlace(self):
        self.departurePlace = input("Enter departure place : ")

class bookAPlane(passengerDetails):
    def getBookingDetails(self):
        self.setPassengerName()
        self.setArrivalPlace()
        self.setDeparturePlace()