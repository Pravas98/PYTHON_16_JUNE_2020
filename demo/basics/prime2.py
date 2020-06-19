# Accept a number and display whether it is prime

num = int(input("Enter a number :"))

for i in range(2, num // 2 + 1):
    if num % i == 0:
        print('Not a prime number because it is divisible by', i)
        break
else:
    print("Prime Number")
