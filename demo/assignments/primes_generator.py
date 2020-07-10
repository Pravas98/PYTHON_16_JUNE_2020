import math


def primes(start, end):
    for n in range(start, end + 1):
        for i in range(2, math.floor(math.sqrt(n)) + 1):
            if n % i == 0:
                break
        else:
            yield n


for n in primes(100, 110):
    print(n)
