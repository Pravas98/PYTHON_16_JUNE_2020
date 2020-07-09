
def numbers():
    for n in range(1,3):
        yield n

def primes(min,max):
    pass


g = numbers()
print(g)
print(next(g))
print(next(g))
print(next(g))

