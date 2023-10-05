#!/usr/bin/python3
"""
This module contains the BaseGeometry class.
"""


class BaseGeometry:
    """
    A class named BaseGeometry.
    """

    def area(self):
        """
        Placeholder method for calculating the area.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.
        Args:
            name (str): The name of the value.
            value (int): The value to be validated.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")