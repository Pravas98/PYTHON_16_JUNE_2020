numbers = [10, 20, 11, 444, 55]

for n in filter(lambda n : n % 2 == 0 ,numbers):
     print(n)

for n in filter(lambda n : n % 2 == 0 and n % 5 == 0 ,numbers):
     print(n)