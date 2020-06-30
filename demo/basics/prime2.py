import sys

# print(sys.argv)
if len(sys.argv) < 2:
    print("Usage : python prime2.py number")
    exit(1)

if not sys.argv[1].isdigit():
    print("Invalid number!")
    exit(2)


num = int(sys.argv[1])

for i in range(2, num // 2 + 1):
    if num % i == 0:
        print('Not a prime number because it is divisible by', i)
        break
else:
    print("Prime Number")
