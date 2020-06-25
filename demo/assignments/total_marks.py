students = {}
while True:
    rollno = int(input("Enter rollno :"))
    if rollno == 0:
        break

    marks = int(input("Enter marks  : "))
    # if rollno in students:
    #     students[rollno] += marks
    # else:
    #     students[rollno] = marks

    students[rollno] = students.get(rollno, 0) + marks

for rollno, total in sorted(students.items()):
    print(rollno, total)
