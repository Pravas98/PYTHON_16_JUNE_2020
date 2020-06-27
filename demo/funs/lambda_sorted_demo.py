names = ['Python', 'Java', 'Ruby', 'TypeScript', 'C', 'JavaScript']

for n in sorted(names, key=lambda v: v[-2:]):
    print(n)

for n in map(lambda v: v[-2:].upper(), names):
    print(n)
