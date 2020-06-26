def iseven(n):
    return n % 2 == 0


def isupper(s):
    return s.isupper()


nums = [10, 20, 11, 77, 80]

for n in filter(iseven, nums):
    print(n)

for c in filter(isupper, 'PyTHon'):
    print(c)

for c in filter(str.isupper, 'PyTHon'):
    print(c)

# for s in filter(  ,  ['abc','xYz','123ABC']):
#     print(s)