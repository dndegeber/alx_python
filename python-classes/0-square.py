#!/usr/bin/python3

"""
This module defines the Square class, which represents a square.

Classes:
    Square: A class representing a square.
"""


class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int): The size of the square.

        Note:
            The size is a private attribute, mangled with double underscores
            to indicate that it's intended for internal use within the class.
        """
        self.__size = size

