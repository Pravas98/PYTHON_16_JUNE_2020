class Student:
    # Constructor
    def __init__(self, name, course, feepaid=0):
        # Object Attributes
        self.name = name
        self.course = course
        self.feepaid = feepaid

    def payment(self, amount):
        """
        Takes amount being paid and increments feepaid
        Params  : amount  - amount being paid
        Returns : None
        """
        self.feepaid += amount

    def get_course_name(self):
        return "Python" if self.course == 1 else "Java"

    def get_course_fee(self):
        return 10000 if self.course == 1 else 15000

    def get_due(self):
        return self.get_course_fee() - self.feepaid

    def print_details(self):
        print(f"Name        : {self.name}")
        print(f"Course      : {self.get_course_name()}")
        print(f"Feepaid     : {self.feepaid}")
        print(f"Due Amount  : {self.get_due()}")


s1 = Student("George Koch", 1)  # create an object
s1.payment(5000)  # call a method
s1.print_details()

s2 = Student("Bob Tabour", 2, 5000)
s2.print_details()
