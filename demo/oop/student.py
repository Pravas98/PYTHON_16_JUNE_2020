class InvalidCourseError(Exception):
    def __init__(self, course=None):
        self.course = course

    def __str__(self):
        return f"Invalid Course Code {self.course}!"


class Student:
    # Class attribute or static attribute
    gst = 18

    @staticmethod
    def get_gst():
        return Student.gst

    # Constructor
    def __init__(self, name, course, feepaid=0):
        # Object Attributes
        self.name = name
        if course not in [1, 2]:
            raise InvalidCourseError(course)

        self.course = course

        if feepaid < 0:
            raise ValueError("Invalid Feepaid. It cannot be negative!")

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

try:
    s1 = Student("George Koch", 3)  # create an object
    s1.payment(5000)  # call a method
    s1.print_details()
except Exception as ex:
    print(ex)


s2 = Student("Bob Tabour", 2, 5000)
s2.print_details()
