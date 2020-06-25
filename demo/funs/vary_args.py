def wish(*names, message='Hello'):
    for n in names:
        print(message, n)


wish('Jack', 'Mike', 'Steve')
wish('Jack', 'Steve', message='Hi')
