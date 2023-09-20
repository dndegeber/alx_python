#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
    """Rectangle class inherited from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x coordinate of the rectangle.
            y (int): The y coordinate of the rectangle.
            id (int): The id for the Rectangle instance.

        Raises:
            ValueError: If any of the arguments `width`, `height`, `x`, or `y`
                is not an integer.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width.

        Args:
            value (int): The value to set for width.

        Raises:
            ValueError: If `value` is not an integer or if it's less than 1.
        """
        if not isinstance(value, int):
            raise ValueError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height.

        Args:
            value (int): The value to set for height.

        Raises:
            ValueError: If `value` is not an integer or if it's less than 1.
        """
        if not isinstance(value, int):
            raise ValueError("height must be an integer")
        if value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x.

        Args:
            value (int): The value to set for x.

        Raises:
            ValueError: If `value` is not an integer or if it's less than 0.
        """
        if not isinstance(value, int):
            raise ValueError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y.

        Args:
            value (int): The value to set for y.

        Raises:
            ValueError: If `value` is not an integer or if it's less than 0.
        """
        if not isinstance(value, int):
            raise ValueError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

