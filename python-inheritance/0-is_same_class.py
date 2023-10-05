#!/usr/bin/python3
"""
Module: 0-is_same_class

Contains a function for checking if an object is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of the specified class; otherwise False.
    """
    return type(obj) is a_class