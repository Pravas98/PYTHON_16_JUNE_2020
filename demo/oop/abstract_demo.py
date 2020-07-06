from abc import ABC, abstractmethod


class Person(ABC):

    @abstractmethod  # method must be overridden in subclass
    def get_occupation(self):
        pass


class Player(Person):
    def __init__(self, game):
        self.game = game

    def get_occupation(self):
        return "Plays " + self.game


class Student(Person):
    def __init__(self, course):
        self.course = course

    def get_occupation(self):
        return "Studies " + self.course


s = Student("MS CS")
print(isinstance(s, Person))
