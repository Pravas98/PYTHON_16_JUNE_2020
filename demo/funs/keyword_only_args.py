# Keyword only args
def details(*, name='', age=0, email=''):
    pass


# details('abc', 10)
# details('xyz', 20, 'xyz@gmail.com')

details(name='Abc', age=30)
