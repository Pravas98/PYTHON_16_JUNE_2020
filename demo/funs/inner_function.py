g = 1000   # Global variable

def fun1():  # Enclosing function
    # Local function
    a = 100  # Enclosing variable
    global g
    g = 2000

    def fun2():
        nonlocal a
        a = a + 1
        b = 200  # Local variable
        print("a = ", a, "b = ", b, "g = ",g)

    fun2()
    print(a)


fun1()
