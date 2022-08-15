number_of_students = 3
number_of_subjects = 3
student_marks = []
gpa_of_each_student = []

for student in range(number_of_students):
    sum_of_marks = 0
    for subject in range(number_of_subjects):
        print("Enter mark for student ", student+1, " in subject ", subject+1)
        subject_mark = int(input())
        student_marks.append(subject_mark)
        sum_of_marks += subject_mark
    gpa_of_the_student = round(sum_of_marks / number_of_subjects)
    gpa_of_each_student.append(gpa_of_the_student)

for gpa in range(number_of_students):
    print("GPA of student ", gpa+1, " is : ", gpa_of_each_student[gpa])

average_of_the_class = round(sum(gpa_of_each_student) / number_of_students)
print("Average of the class is : ", average_of_the_class)