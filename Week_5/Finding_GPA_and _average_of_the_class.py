number_of_students = 3      #initializing number of students to 3
number_of_subjects = 3      #initializing number of subjects to 3
gpa_of_each_student = []    #initializing a list to store gpa of each student

for student in range(number_of_students):       #using for loop to get marks for each student
    sum_of_marks = 0                            #initializing sum of marks to 0
    for subject in range(number_of_subjects):   #using for loop to get marks for each subject
        print("Enter mark for student ", student+1, " in subject ", subject+1)      #printing to let the user enter the mark for the student
        subject_mark = int(input())              #reading mark from the user
        sum_of_marks += subject_mark             #calculating sum of marks by adding sum of marks with the subject mark
    gpa_of_the_student = round(sum_of_marks / number_of_subjects)       #calculating gpa by dividing sum of marks by number of subjects
    gpa_of_each_student.append(gpa_of_the_student)                      #adding the gpa of a student into a list

for gpa in range(number_of_students):                                 #using for loop to print the gpa of the students
    print("GPA of student ", gpa + 1, " is : ", gpa_of_each_student[gpa])    #printing gpa of the students from the list

average_of_the_class = round(sum(gpa_of_each_student) / number_of_students) #calculating average of the class by dividing sum of gpa of the students by number of students in the class
print("Average of the class is : ", average_of_the_class)                   #printing average of the class



#test case 1
#Enter mark for student  1  in subject  1
#90
#Enter mark for student  1  in subject  2
#87
#Enter mark for student  1  in subject  3
#96
#Enter mark for student  2  in subject  1
#68
#Enter mark for student  2  in subject  2
#78
#Enter mark for student  2  in subject  3
#95
#Enter mark for student  3  in subject  1
#67
#Enter mark for student  3  in subject  2
#75 
#Enter mark for student  3  in subject  3
#87
#GPA of student  1  is :  91
#GPA of student  2  is :  80
#GPA of student  3  is :  76
#Average of the class is :  82

#test case 2 with one 0 mark
#Enter mark for student  1  in subject  1
#0
#Enter mark for student  1  in subject  2
#89
#Enter mark for student  1  in subject  3
#87
#Enter mark for student  2  in subject  1
#98
#Enter mark for student  2  in subject  2
#99
#Enter mark for student  2  in subject  3
#100
#Enter mark for student  3  in subject  1
#58
#Enter mark for student  3  in subject  2
#87
#Enter mark for student  3  in subject  3
#90
#GPA of student  1  is :  59
#GPA of student  2  is :  99
#GPA of student  3  is :  78
#Average of the class is :  79
