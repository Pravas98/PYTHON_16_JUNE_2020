from datetime import *

with open("students.txt","rt") as file:
    students = {}
    today = datetime.now()
    for line in file.readlines():
        parts = line.strip().split(",")
        if len(parts) < 2:
            continue
        name = parts[0]
        try:
            dob = datetime.strptime(parts[1],"%Y%m%d")
            age = (today - dob).days // 365
            students[name] = age
        except:
            pass


for name,age in sorted(students.items(), key= lambda t : t[1]):
    print(f"{name:20} {age:3}")