#!/usr/bin/python3
"""
Module: 1-is_kind_of_class

Contains a function for checking if an object is an instance of or inherited from a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or inherited from, a specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of the specified class or inherited from it; otherwise False.
    """
    return isinstance(obj, a_class)