def getSubjectName():                           #function to get subject name
    for subject in range(totalSubjects):        #looping for the number of subjects
        subjectName = input("Enter " + str(subject+1) + " subject name : ")     #reading subject names
        subjectList.append(subjectName)                                         #adding suject name to list
    return subjectList                                                          #returning the subject list

def getMarks():                                 #function to get marks
    for subject in range(totalSubjects):        #looping for number of subjects to get mark for all subjects
        studentMarkList.append([])              #creating a list inside list to store marks for each subjects seperately
        for mark in range(numberOfStudents):    #looping for the number of students to get marks for all students
            studentMark = int(input("Enter mark for student " + str(mark+1) + " in subject " + subjectList[subject] + " : "))                               #reading mark
            studentMarkList[subject].append(studentMark)            #adding mark to the sublist
    return studentMarkList                      #returning mark list that contains sublist of subjects with marks

def computeGrade():                             #function to calculate grade
    for subject in range(totalSubjects):        #looping for number of subjects
        studentGrade.append([])                 #creating a list inside list to store grades for each subjects seperately
        for mark in range(numberOfStudents):    #looping for the number of students
            #calcualting grade and appending it to the corresponding sublist
            if studentMarkList[subject][mark] <= 60:
                studentGrade[subject].append("Fail")
            elif studentMarkList[subject][mark] >90:
                studentGrade[subject].append("A")
            elif studentMarkList[subject][mark] >80:
                studentGrade[subject].append("B")
            elif studentMarkList[subject][mark] >70:
                studentGrade[subject].append("C")
            elif studentMarkList[subject][mark] > 60:
                studentGrade[subject].append("D")
    return studentGrade                         #returning student grade list

def computeAvergeOfClass():                     #function to calculate average of class
    for subject in range(totalSubjects):        #looping for the number of subjects
        classAverage.append([])                 #creating a list inside list to store average of each subjects separately
        for mark in range(numberOfStudents):    #looping for the number of students
            sumOfMarks = sum(studentMarkList[subject])      #calculating sum of marks of one subject
            averageOfTheClass = round(sumOfMarks / numberOfStudents)    #calculating average of that sum
        classAverage[subject].append(subjectList[subject])              #adding subject into the sublist
        classAverage[subject].append(averageOfTheClass)                 #adding corresponding average to the sublist
    return classAverage                                                 #returning class average list

totalSubjects = int(input("Enter total number of subjects : "))         #reading total number of subjects
numberOfStudents = int(input("Enter the total number of students : "))  #reading number of students
#initializing lists for : subject names, student marks, student grades, class average
subjectList = []
studentMarkList = []
studentGrade = []
classAverage = []

subjectList = getSubjectName()          #calling getSubjectName() and getting the names of the subjects
studentMarkList = getMarks()            #calling getMarks() and getting the marks of the students
studentGrade = computeGrade()           #calling computeGrade() and getting the grades of the students
classAverage = computeAvergeOfClass()   #calling computeAverageOfClass() and getting the average of the class

print("Grade of students in each subject : ")
for subject in range(totalSubjects):                            #looping for the number of subjects
    print("Grade of each student in ", subjectList[subject])    #printing subject name
    print(*studentGrade[subject])                     #printing the grade of students in the current subject in the loop
    if subject+1 == totalSubjects:                              #when the last subject is reached
        print("Average of the class : ")                        #printing the average of the class
        for averageMark in classAverage:                        #looping the classAverage list
            print(" ".join(map(str, averageMark)))              #printing the class average with subject name




"""
test case 1 : not rounding the class average
Enter total number of subjects : 2
Enter the total number of students : 3
Enter 1 subject name : English
Enter 2 subject name : Politics
Enter mark for student 1 in subject English : 90
Enter mark for student 2 in subject English : 45
Enter mark for student 3 in subject English : 82
Enter mark for student 1 in subject Politics : 50
Enter mark for student 2 in subject Politics : 98
Enter mark for student 3 in subject Politics : 100
Grade of students in each subject : 
Grade of each student in  English
B Fail B
Grade of each student in  Politics
Fail A A
Average of the class :
English 72.33333333333333
________________________________________________________

test case 2 : rounding the class average
Enter total number of subjects : 5
Enter the total number of students : 10
Enter 1 subject name : Tamil
Enter 2 subject name : English
Enter 3 subject name : Maths
Enter 4 subject name : Environmental science
Enter 5 subject name : Social
Enter mark for student 1 in subject Tamil : 80
Enter mark for student 2 in subject Tamil : 75
Enter mark for student 3 in subject Tamil : 40
Enter mark for student 4 in subject Tamil : 20
Enter mark for student 5 in subject Tamil : 90
Enter mark for student 6 in subject Tamil : 75
Enter mark for student 7 in subject Tamil : 54
Enter mark for student 8 in subject Tamil : 60
Enter mark for student 9 in subject Tamil : 75
Enter mark for student 10 in subject Tamil : 12
Enter mark for student 1 in subject English : 98
Enter mark for student 2 in subject English : 94
Enter mark for student 3 in subject English : 93
Enter mark for student 4 in subject English : 0
Enter mark for student 5 in subject English : 78
Enter mark for student 6 in subject English : 47
Enter mark for student 7 in subject English : 12
Enter mark for student 8 in subject English : 88
Enter mark for student 9 in subject English : 87
Enter mark for student 10 in subject English : 97
Enter mark for student 1 in subject Maths : 100
Enter mark for student 2 in subject Maths : 98
Enter mark for student 3 in subject Maths : 97
Enter mark for student 4 in subject Maths : 58
Enter mark for student 5 in subject Maths : 64
Enter mark for student 6 in subject Maths : 84
Enter mark for student 7 in subject Maths : 77
Enter mark for student 8 in subject Maths : 83
Enter mark for student 9 in subject Maths : 85
Enter mark for student 10 in subject Maths : 95
Enter mark for student 1 in subject Environmental science : 91
Enter mark for student 2 in subject Environmental science : 90
Enter mark for student 3 in subject Environmental science : 86
Enter mark for student 4 in subject Environmental science : 84
Enter mark for student 5 in subject Environmental science : 75
Enter mark for student 6 in subject Environmental science : 71
Enter mark for student 7 in subject Environmental science : 94
Enter mark for student 8 in subject Environmental science : 73
Enter mark for student 9 in subject Environmental science : 54
Enter mark for student 10 in subject Environmental science : 68
Enter mark for student 1 in subject Social : 90
Enter mark for student 2 in subject Social : 99
Enter mark for student 3 in subject Social : 84
Enter mark for student 4 in subject Social : 86
Enter mark for student 5 in subject Social : 87
Enter mark for student 6 in subject Social : 82
Enter mark for student 7 in subject Social : 80
Enter mark for student 8 in subject Social : 94
Enter mark for student 9 in subject Social : 94
Enter mark for student 10 in subject Social : 91
Grade of students in each subject : 
Grade of each student in  Tamil
C C Fail Fail B C Fail Fail C Fail
Grade of each student in  English
A A A Fail C Fail Fail B B A
Grade of each student in  Maths
A A A Fail D B C B B A
Grade of each student in  Environmental science
A B B B C C A C Fail D
Grade of each student in  Social
B A B B B B C A A A
Average of the class :
Tamil 58
English 69
Maths 84
Environmental science 79
Social 89
"""