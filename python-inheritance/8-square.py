
from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size):
        self.__size = super().integer_validator("size", size)
        super().__init__(self.__size, self.__size)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)







