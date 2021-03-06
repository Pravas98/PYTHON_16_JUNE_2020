from datetime import *
import re

with open("students2.txt", "rt") as file:
    students = {}
    today = datetime.now()
    for line in file.readlines():
        # remove all non-digit, non-alpha and non-space chars
        line = re.sub(r"[^0-9A-Za-z ]",'',line)
        m = re.search(r"[A-Za-z ]+", line)
        if m is None:  # Name not found
            continue
        else:
            name = m.group().strip()

        # look for dob
        m = re.search(r"\d+", line)
        if m is None:  # DOB not found
            continue
        else:
            dobstr = m.group()

        try:
            dob = datetime.strptime(dobstr, "%Y%m%d")
            age = (today - dob).days // 365
            students[name] = age
        except:
            pass

for name, age in sorted(students.items(), key=lambda t: t[1]):
    print(f"{name:20} {age:3}")
