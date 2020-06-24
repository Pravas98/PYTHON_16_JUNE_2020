def print_factors(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            print(i)


def iseven(n):
    return n % 2 == 0


print_factors(30)
print(iseven(30))
