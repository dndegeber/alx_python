#!/usr/bin/python3
"""
Contains a function for checking if an object
is an instance of a class that inherited from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a
    class that inherited from a specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of a class
        that inherited from the specified class; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class