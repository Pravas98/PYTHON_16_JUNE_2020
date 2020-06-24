names = ['Python', 'Java', 'C#','TypeScript']
vers = [3.8, 14, 9]

# for idx, n in enumerate(names):
#     print(n, vers[idx])

for n, v in zip(names, vers):
    print(n, v)
