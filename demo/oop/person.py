class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # private attribute

    def print_details(self):
        print(self.name, self.__age)


p1 = Person("Abc", 20)
p1._Person__age = 30  # Accessing private attribute
p1.print_details()
p1.gender = "Male"
print(p1.__dict__)

