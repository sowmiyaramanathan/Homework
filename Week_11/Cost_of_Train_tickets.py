def getAge():
    for person in range(numberOfTickets):
        age = int(input("Enter your age to check for seniority : "))
        ageOfPassengers.append(age)
    return ageOfPassengers

def calculateFare():
    for age in range(len(ageOfPassengers)):
        if ageOfPassengers[age] >= 60:
            ticketFareOfPassengers.append(ticketFare / 2)
        else:
            ticketFareOfPassengers.append(ticketFare)
    totalFare = sum(ticketFareOfPassengers)
    if numberOfReturnTicket != 0:
        totalReturnTicketFare = numberOfReturnTicket * (returnTicketFare + ticketFare)
        totalFare += totalReturnTicketFare
    if numberOfTickets >=4:
        applyDiscount = 20 / 100
        totalFare -= (totalFare * applyDiscount)
    return totalFare

print("Ticket fare from Madurai to Chennai (vice versa) is Rs.1000. \nBooking a return ticket costs extra Rs.750 \nFamily of 4 or above gets 20% off \nSenior citizens can get 50% off")
numberOfTickets = int(input("Enter total number of tickets : "))
numberOfReturnTicket = int(input("Do you want to book a return ticket? If yes, enter how many. Otherwise press '0' : "))
ticketFare = 1000
returnTicketFare = 750
ageOfPassengers = []
ticketFareOfPassengers = []

ageOfPassengers = getAge()
totalTicketCost = calculateFare()
print("Total cost of tickets : Rs.", totalTicketCost)



"""
test case 1 - with seniority, return ticket, family of >= 4
Ticket fare from Madurai to Chennai (vice versa) is Rs.1000. 
Booking a return ticket costs extra Rs.750
Family of 4 or above gets 20% off
Senior citizens can get 50% off
Enter total number of tickets : 5
Do you want to book a return ticket? If yes, enter how many. Otherwise press '0' : 2
Enter your age to check for seniority : 18
Enter your age to check for seniority : 20
Enter your age to check for seniority : 21
Enter your age to check for seniority : 40
Enter your age to check for seniority : 67
Total cost of tickets : Rs. 6400.0
__________________________________________________________

test case 2 - without - seniority, return ticket, family of >= 4
Ticket fare from Madurai to Chennai (vice versa) is Rs.1000. 
Booking a return ticket costs extra Rs.750
Family of 4 or above gets 20% off
Senior citizens can get 50% off
Enter total number of tickets : 3
Do you want to book a return ticket? If yes, enter how many. Otherwise press '0' : 0
Enter your age to check for seniority : 24
Enter your age to check for seniority : 27
Enter your age to check for seniority : 25
Total cost of tickets : Rs. 3000
___________________________________________________________

test case 3 - only seniority
Ticket fare from Madurai to Chennai (vice versa) is Rs.1000. 
Booking a return ticket costs extra Rs.750
Family of 4 or above gets 20% off
Senior citizens can get 50% off
Enter total number of tickets : 2
Do you want to book a return ticket? If yes, enter how many. Otherwise press '0' : 0
Enter your age to check for seniority : 65
Enter your age to check for seniority : 61
Total cost of tickets : Rs. 1000.0
___________________________________________________________

test case 4 - only return
Ticket fare from Madurai to Chennai (vice versa) is Rs.1000. 
Booking a return ticket costs extra Rs.750
Family of 4 or above gets 20% off
Senior citizens can get 50% off
Enter total number of tickets : 1
Do you want to book a return ticket? If yes, enter how many. Otherwise press '0' : 1
Enter your age to check for seniority : 50
Total cost of tickets : Rs. 2750
___________________________________________________________

test case 5 - only family
Ticket fare from Madurai to Chennai (vice versa) is Rs.1000. 
Booking a return ticket costs extra Rs.750
Family of 4 or above gets 20% off
Senior citizens can get 50% off
Enter total number of tickets : 4
Do you want to book a return ticket? If yes, enter how many. Otherwise press '0' : 0
Enter your age to check for seniority : 40
Enter your age to check for seniority : 37
Enter your age to check for seniority : 24
Enter your age to check for seniority : 12
Total cost of tickets : Rs. 3200.0
___________________________________________________________

test case 6 - seniority and return
Ticket fare from Madurai to Chennai (vice versa) is Rs.1000. 
Booking a return ticket costs extra Rs.750
Family of 4 or above gets 20% off
Senior citizens can get 50% off
Enter total number of tickets : 2
Do you want to book a return ticket? If yes, enter how many. Otherwise press '0' : 1
Enter your age to check for seniority : 60
Enter your age to check for seniority : 54
Total cost of tickets : Rs. 3250.0
___________________________________________________________

test case 7 - seniority and family
Ticket fare from Madurai to Chennai (vice versa) is Rs.1000. 
Booking a return ticket costs extra Rs.750
Family of 4 or above gets 20% off
Senior citizens can get 50% off
Enter total number of tickets : 6
Do you want to book a return ticket? If yes, enter how many. Otherwise press '0' : 0
Enter your age to check for seniority : 75
Enter your age to check for seniority : 70
Enter your age to check for seniority : 54
Enter your age to check for seniority : 50
Enter your age to check for seniority : 30
Enter your age to check for seniority : 24
Total cost of tickets : Rs. 4000.0
___________________________________________________________

test case 8 - return and family
Ticket fare from Madurai to Chennai (vice versa) is Rs.1000. 
Booking a return ticket costs extra Rs.750
Family of 4 or above gets 20% off
Senior citizens can get 50% off
Enter total number of tickets : 4
Do you want to book a return ticket? If yes, enter how many. Otherwise press '0' : 4
Enter your age to check for seniority : 50
Enter your age to check for seniority : 45
Enter your age to check for seniority : 24
Enter your age to check for seniority : 21
Total cost of tickets : Rs. 8800.0
"""