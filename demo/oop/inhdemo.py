class Programmer:
    def __init__(self, name, email, lang):
        self.name = name
        self.email = email
        self.lang = lang

    def print_details(self):
        print(f"Name     : {self.name}")
        print(f"Email    : {self.email}")
        print(f"Language : {self.lang}")

    def get_lang(self):
        return self.lang


class Consultant(Programmer):
    def __init__(self, name, email, lang, hours, rate):
        super().__init__(name, email, lang)
        self.hours = hours
        self.rate = rate

    # Override print_details of super class
    def print_details(self):
        super().print_details()
        print(f"Hours    : {self.hours}")
        print(f"Rate     : {self.rate}")

    def get_salary(self):
        return self.hours * self.rate


c = Consultant("James", "james@gmail.com", "Python", 20, 1000)
c.print_details()
print(c.get_salary())
print(c.get_lang())
