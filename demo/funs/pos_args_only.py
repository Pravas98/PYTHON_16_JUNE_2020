def fun(a, b, /):
    pass


def fun2(message):
    pass


fun(10, 20)
# fun(a=10, b=20)   # cannot be done as a and b are positional only
fun2(message="abc")
