def openToBook():                                                           #function to check if booking is open
    open = input("Open to book tickets? Yes/No : ")                         #reading input for open or close
    if(open == "No"):
        print("Total weekend bookings for today : ", weekendCount)          #if no, printing weekend booking count
        exit()                                                              #and closing booking
    else:
        startBooking = True                                                 #else setting response as open
    return startBooking                                                     #sending the response
    
def getBookingDetails():                                      #function to get age and time of day of travel
    global weekendCount                                       #variable to count weekend bookings
    print("Ticket fare from Madurai to Chennai (vice versa) is \nFor weekday morning or afternoon Rs.3500 \nFor weekday evening Rs.3000 \nFor weekend Rs.5000 \nSenior citizens can get 10% off \n20% off for bookings prior two weeks")                                                #printing booking information
    
    numberOfTickets = int(input("Enter total number of tickets : "))    #reading number of tickets
    for passenger in range(numberOfTickets):                    #iterating for total tickets times
        print("Enter details for passenger ", passenger + 1)
        flight = input("weekday or weekend flight : ")  #reading input for weekend or weekday as fare depends on it
        if flight == "weekday":
            time = input("morning, afternoon, or evening : ")   #asking for time of the day if it is weekday
            flightBooked.append(time)  #adding the time of day to the coreesponsing list to get the respective fare
        else:
            weekendCount += 1                         #increasing the weekend booking count if it is not on weekday
            flightBooked.append(flight)                 #adding weekend to the coreesponsing list to get the fare
        age = int(input("Enter the age to check for seniority : "))   #reading age to see if discount is applicable
        passengerAge.append(age)                                        #adding age to the corresponding list

def calculateFare(age, time):                                       #function to calculate ticket fare
    flightDue = int(input("Your flight is due in (how many days): "))   #reading for flight due to apply discount
    if time in flightTiming:                                    #checking if the time of the day exists in the dictionary to get the corresponding ticket amount
        ticketFare = flightTiming[time]                         #getting ticket fare
        if age >= seniorAge:                                    #checking if the passenger is a senior citizen
            applyDiscount = 10 / 100                            #setting discount value
            ticketFare -= (ticketFare * applyDiscount)          #applying discount on the ticket fare 
    if flightDue > 14:                                          #checking if the flight is booked before 2 weeks
        applyDiscount = 20 / 100                                #setting discount value
        ticketFare -= (ticketFare * applyDiscount)              #applying discount on the ticket fare 
    ticketFareOfPassengers.append(ticketFare)                   #adding the ticket fare to the respective list


flightTiming = {"morning" : 3500, "afternoon" : 3500, "evening" : 3000, "weekend":5000}  #time of day and their associated ticket fare   
seniorAge = 60                                                  #variable denoting age of senior citizen
weekendCount = 0                                                #variable to track weekend bookings count


openBooking = openToBook()                           #calling openToBook function to check whether booking is open
while(openBooking == True):                          #till the response is true, allow passengers to book tickets
    passengerAge = []                                #list to store age of passengers to check for seniority
    flightBooked = []                 #list to store which time of the day, the passenger wants to book the flight
    ticketFareOfPassengers = []                      #list that stores the fare of each tickets
    getBookingDetails()               #calling getBookingDetails function to get age and time of the day of flight
    for passenger in range(len(flightBooked)):       #iterating for the length of the flightBooked list to calculate fare of each tickets booked
        print("Passenger ", passenger + 1)
        calculateFare(passengerAge[passenger], flightBooked[passenger]) #calling calculateFare function to calculate fare of the tickets while applying discount also
    totalTicketFare = sum(ticketFareOfPassengers)                       #calculating total fare of the tickets
    print("Total cost of tickets : Rs.", totalTicketFare)               #printing the total fare

    openToBook()                                           #calling function to check whether the booking is open



"""
test case 1
Open to book tickets? Yes/No : Yes
Ticket fare from Madurai to Chennai (vice versa) is 
For weekday morning or afternoon Rs.3500 
For weekday evening Rs.3000 
For weekend Rs.5000 
Senior citizens can get 10% off
20% off for bookings prior two weeks
Enter total number of tickets : 5
Enter details for passenger  1
weekday or weekend flight : weekday
morning, afternoon, or evening : morning
Enter the age to check for seniority : 61
Enter details for passenger  2
weekday or weekend flight : weekday
morning, afternoon, or evening : morning
Enter the age to check for seniority : 40
Enter details for passenger  3
weekday or weekend flight : weekday
morning, afternoon, or evening : morning
Enter the age to check for seniority : 21
Enter details for passenger  4
weekday or weekend flight : weekend
Enter the age to check for seniority : 20
Enter details for passenger  5
weekday or weekend flight : weekend
Enter the age to check for seniority : 18
Passenger  1
Your flight is due in (how many days): 20
Passenger  2
Your flight is due in (how many days): 20
Passenger  3
Your flight is due in (how many days): 20
Passenger  4
Your flight is due in (how many days): 10
Passenger  5
Your flight is due in (how many days): 10
Total cost of tickets : Rs. 18120.0
Open to book tickets? Yes/No : No 
Total weekend bookings for today :  2
_________________________________________________________________

test case 2
Open to book tickets? Yes/No : Yes
Ticket fare from Madurai to Chennai (vice versa) is 
For weekday morning or afternoon Rs.3500
For weekday evening Rs.3000
For weekend Rs.5000
Senior citizens can get 10% off
20% off for bookings prior two weeks
Enter total number of tickets : 2
Enter details for passenger  1
weekday or weekend flight : weekday
morning, afternoon, or evening : evening
Enter the age to check for seniority : 27
Enter details for passenger  2
weekday or weekend flight : weekday
morning, afternoon, or evening : evening
Enter the age to check for seniority : 24
Passenger  1
Your flight is due in (how many days): 15
Passenger  2
Your flight is due in (how many days): 15
Total cost of tickets : Rs. 4800.0
Open to book tickets? Yes/No : Yes
Ticket fare from Madurai to Chennai (vice versa) is 
For weekday morning or afternoon Rs.3500
For weekday evening Rs.3000
For weekend Rs.5000
Senior citizens can get 10% off
20% off for bookings prior two weeks
Enter total number of tickets : 1
Enter details for passenger  1
weekday or weekend flight : weekend
Enter the age to check for seniority : 67
Passenger  1
Your flight is due in (how many days): 15
Total cost of tickets : Rs. 3600.0
Open to book tickets? Yes/No : No
Total weekend bookings for today :  1
__________________________________________________________

test case 3
Open to book tickets? Yes/No : No
Total weekend bookings for today :  0
_________________________________________________________


"""