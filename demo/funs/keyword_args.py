
def details(**properties):
    for k,v in properties.items():
        print(k,v)


details(name='Abc', age = 30, weight=60)
details(name='Abc', email='abc@gmail.com')