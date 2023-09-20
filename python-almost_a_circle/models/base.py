# models/base.py

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

# 0-main.py

from models.base import Base

if __name__ == "__main__":
    b1 = Base()
    print(b1.id)  # Output: 1

    b2 = Base()
    print(b2.id)  # Output: 2

    b3 = Base()
    print(b3.id)  # Output: 3

    b4 = Base(12)
    print(b4.id)  # Output: 12

    b5 = Base()
    print(b5.id)  # Output: 4
