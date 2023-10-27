#!/usr/bin/python3
"""
This module contains the Square class that inherits from Rectangle.
"""

Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """
    A class named Square that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.
        Args:
            size (int): The size of the square.
        """
        # Validate and set size using the integer_validator method
        self.integer_validator("size", size)
        # Call the constructor of the parent class Rectangle
        # with size for both width and height
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return "[Square] {}/{}".format(
            self._Rectangle__width,
            self._Rectangle__height
        )


