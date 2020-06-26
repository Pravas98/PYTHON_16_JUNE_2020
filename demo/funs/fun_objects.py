def add(a, b):
    return a + b

print(type(add))

add2 = add


def add(a, b, c):
    return a + b + c


print(add2(10, 20))
print(add(20, 30, 30))
