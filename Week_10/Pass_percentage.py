numberOfSubjects = int(input("Enter number of subjects : "))
subjectMark = []
for subject in range(numberOfSubjects):
    mark = int(input("Enter mark for subject: "))
    subjectMark.append(mark)

def calculateResult(subjectMark):
    count_40 = 0
    count_80 = 0
    count_90 = 0
    count_between = 0
    for mark in range(len(subjectMark)):
        if(subjectMark[mark] <= 100):
            if(subjectMark[mark] < 40):
                count_40 += 1
            else:
                if(subjectMark[mark] > 90):
                    count_90 += 1
                    count_80 += 1
                    count_between += 1
                elif(subjectMark[mark] > 80):
                    count_80 += 1
                    count_between += 1
                else:
                    count_between += 1
    if(count_90 == numberOfSubjects):
        return "Distinction"
    elif(count_80 == numberOfSubjects):
        return "First class"
    elif(count_between == numberOfSubjects):
        return "Second class"
    elif(count_40 == numberOfSubjects):
        return "Fail"

result = calculateResult(subjectMark)
print("Result is : ", result)