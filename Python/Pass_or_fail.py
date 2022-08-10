subjects = []                               #initializing subjects list to store the marks of students
for mark in range(5):                       #using for loop five times to get five subjects mark
    subject_mark = int(input("Enter the student mark for subject : "))          #reading ssubject mark from the user
    subjects.append(subject_mark)                                               #using append function to add the marks into the list

count_for_90 = 0                        #initializing count to 0, to count the number of subjects where the student has scored above 90
count_for_40 = 0                        #initializing count to 0, to count the number of subjects where the student has scored above 40

for mark in range(5):                   #using for loop five times to check whether the subject mark is 90 or above, or 40 or above
    if(subjects[mark] >= 90):           #using if to check whether the mark is greater than or equal to 90
        count_for_90 += 1               #increasing count for 90 by 1
        count_for_40 += 1               #increasing count for 40 by 1
    elif(subjects[mark] >= 40):         #using if to check whether the mark is greater than or equal to 90
        count_for_40 += 1               #increasing count for 40 by 1

if(count_for_90>=3 and count_for_40>=2):        #using if to check if the student has scored 90 or above in 3 or more subjects and 40 or above in 2 or more subjects
    print("Student passed the degree")          #printing that the student has passed the degree
else:                                           #using else to indicate that the student has not obtained the required scores
    print("Student failed in the degree")       #printing that the student has not passed the degree