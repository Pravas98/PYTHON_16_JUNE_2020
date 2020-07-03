class Line:
    def __init__(self, x, y, width):
        self.__x = x
        self.__y = y
        self.__width = width

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("Invalid value for X")

        self.__x = value


l = Line(10, 20, 50)
l.x = 20
print(l.x)  # Take value from property
