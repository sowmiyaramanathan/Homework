students = []
sum_of_marks = 0

total_students = int(input("Enter total number of students : "))
for student in range(total_students):
    student_name = input("Enter student name : ")
    students.append(student_name)

for student in range(total_students-1, -1, -1):
    mark = int(input("Enter " + str(students[student]) + "'s mark in maths : "))
    sum_of_marks += mark

average_of_the_class = sum_of_marks / total_students
print("Average of the class : ", average_of_the_class)



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