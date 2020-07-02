class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x},{self.y}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        if self.x > other.x:
            return True
        elif self.x < other.x:
            return False
        elif self.y > other.y:
            return True
        else:
            return False

    def __int__(self):
        return self.x * self.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


p1 = Point(10, 20)
p2 = Point(10, 20)
p3 = Point(5, 30)
print(p1, str(p1), p1.__str__())
print(p1 == p2)  # p1.__eq__(p2)
print(p1 > p3)
print(int(p1))
