squares = []

for i in range(1, 11):
    squares.append(i * i)

print(squares)

squares = [n * n for n in range(1, 11)]
print(squares)

# List of codes for uppercase letters
s = "Python is FUN"
code = [ord(ch) for ch in s if ch.isupper()]
print(code)
