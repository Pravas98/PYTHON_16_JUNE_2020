
nums = []

for i in range(5):
    try:
        n = int(input("Enter number :"))
        nums.append(n)
    except ValueError:
        pass

print(sorted(nums))