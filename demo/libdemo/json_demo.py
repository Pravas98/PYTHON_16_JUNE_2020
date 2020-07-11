import json


class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} - {self.email}"


p = Person('Tom Hanks', 'tom@gmail.com')
jsonstring = json.dumps(p.__dict__)  # Dict to JSON
obj = json.loads(jsonstring)  # JSON to dict
print(obj)
