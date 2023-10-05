#!/usr/bin/python3
"""
Contains an empty class definition for BaseGeometry.
"""


class BaseGeometry:
    """
    An empty class representing the base geometry.
    """
    def __init_subclass__(cls):
        pass

    def __dir__(self):
        return [attr for attr in dir(type(self)) if attr != '__init_subclass__']

    def __class__(self):
        return type(self)