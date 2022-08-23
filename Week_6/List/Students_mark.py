students = []       #initializing a list to store the name of the students
sum_of_marks = 0    #initializing sum of the marks as 0

total_students = int(input("Enter total number of students : "))    #reading total number of students
for student in range(total_students):           #using for loop to get the name of the students
    student_name = input("Enter student name : ")   #reading name from the user
    students.append(student_name)                   #adding the name into the students list

for student in range(total_students-1, -1, -1):     #using for to loop through the list in reverse order
    mark = int(input("Enter " + str(students[student]) + "'s mark in maths : "))    #reading mark for the current student
    sum_of_marks += mark               #calculating sum of marks by adding it with the mark of the current student

average_of_the_class = sum_of_marks / total_students        #calculating average of the class
print("Average of the class : ", average_of_the_class)      #printing the average of the class



# test case 1
# Enter total number of students : 5
# Enter student name : Kamali
# Enter student name : Surya
# Enter student name : Sam
# Enter student name : David
# Enter student name : Tiana
# Enter Tiana's mark in maths : 95
# Enter David's mark in maths : 90
# Enter Sam's mark in maths : 94
# Enter Surya's mark in maths : 91
# Enter Kamali's mark in maths : 96
# Average of the class :  93.2