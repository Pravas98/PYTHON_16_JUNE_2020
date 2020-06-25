def line(length=10, ch='-'):
    print(ch * length)


line()
line(30, '*')
line(10, '*')  # Positional parameters
line(ch='*', length=20)  # keyword argument
