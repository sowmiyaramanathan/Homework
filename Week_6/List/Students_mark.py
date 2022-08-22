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