subjects = []                               #initializing subjects list to store the marks of students
total_number_of_subjects = 5                #initializing the number of subjects to 5
for mark in range(total_number_of_subjects):            #using for loop five times to get five subjects mark
    subject_mark = int(input("Enter the student mark for subject : "))          #reading subject mark from the user
    subjects.append(subject_mark)                                               #using append function to add the marks into the list

count_for_60 = 0         #initializing count to 0, to count the number of subjects where the student has scored above 60
count_for_90 = 0         #initializing count to 0, to count the number of subjects where the student has scored above 90
count_for_40 = 0         #initializing count to 0, to count the number of subjects where the student has scored above 40
count_for_75 = 0         #initializing count to 0, to count the number of subjects where the student has scored above 75
count_for_50 = 0         #initializing count to 0, to count the number of subjects where the student has scored above 50

for mark in range(total_number_of_subjects):                   #using for loop five times to check whether the subject mark is 90 or above, or 40 or above
    if(subjects[mark] >= 90):           #using if to check whether the mark is greater than or equal to 90
        count_for_90 += 1               #increasing count for 90 by 1
        count_for_75 += 1               #increasing count for 75 by 1
        count_for_60 += 1               #increasing count for 60 by 1
    elif(subjects[mark] >= 75):         #using elif to check whether the mark is greater than or equal to 75
        count_for_75 += 1               #increasing count for 75 by 1
        count_for_60 += 1               #increasing count for 60 by 1
    elif(subjects[mark] > 60):          #using elif to check whether the mark is greater than or equal to 60
        count_for_60 += 1               #increasing count for 60 by 1
    elif(subjects[mark] >= 50 and count_for_75 <= 3):         #using elif to check whether the mark is greater than or equal to 50 and student has scored above 75 in of minimum 3 subjects
        count_for_50 += 1               #increasing count for 50 by 1
        count_for_40 += 1               #increasing count for 40 by 1
    elif(subjects[mark] >= 40 and count_for_90 <= 3):         #using if to check whether the mark is greater than or equal to 40 and student has scored above 90 in of minimum 3 subjects
        count_for_40 += 1               #increasing count for 40 by 1

if(count_for_60 == 5 or (count_for_90 >= 3 and count_for_40 >= 2) or (count_for_75 >= 3 and count_for_50 >= 2)):     #using if to check whether the student has scored (above 60 in all subjects) or (scored 90 or above in 3 or more subjects and 40 or above in 2 or more subjects) or (scored 75 or above in 3 or more subjects and 50 or above in 2 or more subjects)
    print("Student passed the degree")              
else:                                           #using else to indicate that the student has not obtained the required scores
    print("Student failed in the degree")       #printing that the student has not passed the degree