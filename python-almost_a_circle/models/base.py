#!/usr/bin/python3
"""Some module documentation"""

class Base:
    """Some class documentation."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new instance.

        Args:
            id (int, optional): Unique identifier. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

