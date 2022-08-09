subjects = []
for i in range(5):
    subject_mark = int(input("Enter the student mark for subject : "))
    subjects.append(subject_mark)

count = 0
subcount = 0

for i in range(5):
    if(subjects[i] >= 90):
        count += 1
        subcount += 1
    elif(subjects[i] >= 40):
        subcount += 1

if(count>=3 and subcount>=2):
    print("Student passed the degree")
else:
    print("Student failed in the degree")