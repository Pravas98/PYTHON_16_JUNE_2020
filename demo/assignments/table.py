# Display table for the given number

num = int(input("Enter a number :"))

for i in range(1, 11):
    print(f"{num:2} * {i:2} = {num * i:4}")