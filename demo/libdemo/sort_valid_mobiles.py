def is_valid_mobile(n):
    if not n.isdigit():
        return False

    if len(n) == 10:
        return True
    elif len(n) == 12 and n.startswith('91'):
        return True
    else:
        return False


f = open("mobiles.txt", "rt")

mobiles = set()

for line in f.readlines():
    numbers = line.strip().split(",")
    for n in numbers:
        if is_valid_mobile(n):
            mobiles.add(n)

for n in sorted(mobiles):
    print(n)

f.close()