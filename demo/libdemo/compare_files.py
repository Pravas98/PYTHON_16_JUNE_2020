filename1 = "names.txt"
filename2 = "newnames.txt"

f1 = open(filename1, "rt")
f2 = open(filename2, "rt")

str1 = f1.read()
str2 = f2.read()

if str1 == str2:
    print("Files are same!")
    exit(0)

lineno = 1
colno = 1
for ch1, ch2 in zip(str1, str2):
    if ch1 != ch2:
        print(f"Differ at {lineno}, {colno}")
        exit()

    if ch1 == '\n':
        lineno += 1
        colno = 1
    else:
        colno += 1

print(f"Differ at {lineno},{colno}")