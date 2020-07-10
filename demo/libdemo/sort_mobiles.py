f = open("mobiles.txt", "rt")

mobiles = set()

for line in f.readlines():
    numbers = line.strip().split(",")
    mobiles = mobiles.union(numbers)

for n in sorted(mobiles):
    print(n)
