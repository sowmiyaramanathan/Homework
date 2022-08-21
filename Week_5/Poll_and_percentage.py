count_for_onlineclass_from_female = 0               #initializing the count of of female students whose answer would be online class to 0
count_for_responses = 0                             #initializing total count of responses to 0
min_number_of_students = 10                         #initializing minimum of students to 10 (atleast 10)

for student in range(min_number_of_students):       #using got to get the response from the users
    print("Select\n1.Male\n2.Female")               #priting selection menu to know the gender of the student
    gender = input()                                #reading input from the user
    print("Which one do you like?\n1.Online class\n2.In person class\n3.Mixed\nTo end, enter 'No Comment'")     #printing selection menu to tell the user to give his/her response
    answer = input()                                #reading the answer or response from the user
    count_for_responses += 1                        #increasing the total count of responses by 1
    if(answer == "No Comment"):                     #using if to check whether the user given No Comment as input
        break                                       #using break to stop asking for the input i.e.,exiting for loop
    if(gender == "Female" and answer == "Online class"):    #using if to check whether the student is female and her response is online class
        count_for_onlineclass_from_female +=1               #increasing the count of female students whose answer was online class

percentage = count_for_onlineclass_from_female * 100 / count_for_responses      #calculating the percentage of response of female students whose answer was online class by multiplying the number of such answers with 100 and diving it by total count of responses
print(percentage, "% of female students like online class")            #printing the percentage



#test case with ten entries
#Select
#1.Male
#2.Female
#Male
#Which one do you like?
#1.Online class
#2.In person class
#3.Mixed
#To end, enter 'No Comment'
#Mixed
#Select
#1.Male
#2.Female
#Male
#Which one do you like?
#1.Online class
#2.In person class
#3.Mixed
#To end, enter 'No Comment'
#Mixed
#Select
#1.Male
#2.Female
#Male
#Which one do you like?
#1.Online class
#2.In person class
#3.Mixed
#To end, enter 'No Comment'
#Online class
#Select
#1.Male
#2.Female
#Female
#Which one do you like?
#1.Online class
#2.In person class
#3.Mixed
#To end, enter 'No Comment'
#Online class
#Select
#1.Male
#2.Female
#Female
#Which one do you like?
#1.Online class
#2.In person class
#3.Mixed
#To end, enter 'No Comment'
#In person class
#Select
#1.Male
#2.Female
#Female
#Which one do you like?
#1.Online class
#2.In person class
#3.Mixed
#To end, enter 'No Comment'
#Mixed
#Select
#1.Male
#2.Female
#Female
#Which one do you like?
#1.Online class
#2.In person class
#3.Mixed
#To end, enter 'No Comment'
#Online class
#Select
#1.Male
#2.Female
#Male
#Which one do you like?
#1.Online class
#2.In person class
#3.Mixed
#To end, enter 'No Comment'
#Mixed
#Select
#1.Male
#2.Female
#Male
#Which one do you like?
#1.Online class
#2.In person class
#3.Mixed
#To end, enter 'No Comment'
#Mixed
#Select
#1.Male
#2.Female
#Female
#Which one do you like?
#1.Online class
#2.In person class
#3.Mixed
#To end, enter 'No Comment'
#Online class
#30.0 % of female students like online class

#test case with no comment in one response
#Select
#1.Male
#2.Female
#Male
#Which one do you like?
#1.Online class
#2.In person class
#3.Mixed
#To end, enter 'No Comment'
#Mixed
#Select
#1.Male
#2.Female
#Female
#Which one do you like?
#1.Online class
#2.In person class
#3.Mixed
#To end, enter 'No Comment'
#Online class
#Select
#1.Male
#2.Female
#Male
#Which one do you like?
#1.Online class
#2.In person class
#3.Mixed
#To end, enter 'No Comment'
#Online class
#Select
#1.Male
#2.Female
#Female
#Which one do you like?
#1.Online class
#2.In person class
#3.Mixed
#To end, enter 'No Comment'
#Online class
#Select
#1.Male
#2.Female
#Male
#Which one do you like?
#1.Online class
#2.In person class
#3.Mixed
#To end, enter 'No Comment'
#Mixed
#Select
#1.Male
#2.Female
#Female
#Which one do you like?
#1.Online class
#2.In person class
#3.Mixed
#To end, enter 'No Comment'
#In person class
#Select
#1.Male
#2.Female
#Female
#Which one do you like?
#1.Online class
#2.In person class
#3.Mixed
#To end, enter 'No Comment'
#Online class
#Select
#1.Male
#2.Female
#Male
#Which one do you like?
#1.Online class
#2.In person class
#3.Mixed
#To end, enter 'No Comment'
#No Comment
#37.5 % of female students like online class
