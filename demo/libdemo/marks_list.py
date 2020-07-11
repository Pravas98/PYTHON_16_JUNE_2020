with open("marks.txt", "rt") as f:
    students = []
    for line in f.readlines():
        parts = line.strip().split(",")
        if len(parts) <= 1:
            continue  # ignore line

        name = parts[0]
        total = sum(map(int, filter(str.isdigit, parts[1:])))
        average = total / (len(parts) - 1)
        students.append((name, total, average))

for name, total, average in sorted(students):
    print(f"{name:10} {total:3}  {average:.2f}")
