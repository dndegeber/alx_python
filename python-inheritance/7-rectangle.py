
"""
created an empty class
"""
class BaseMeta(type):
     """
     created a BaseMeta class
     """
     def __dir__(self):
        x = super().__dir__()
        list= [item for item in x if item != "__init_subclass__"]
        return list
     
class BaseGeometry(metaclass=BaseMeta):
    """
    created a class called BaseGeometry
    """
    def __dir__(self):
        x = super().__dir__()
        list= [item for item in x if item != "__init_subclass__"]
        return list
    
    def area(self):
        """
        this function raises an exception 
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        validates if the value entered is an integer 

        Arg: 
           value to be validated 
           name is set to be a string
        Returns:
           Exception is raised  if the value entered is not an integer 
           or the value is should be greater than 0

        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            return value

class Rectangle(BaseGeometry):
    """
    Rectangle class
    """

    
    def __init__(self, width, height):
      
      """
      Arg: 
        width is validated to see if it is an integer or not
        height is also validated using the integer_validator method 
      """
      self.__width= super().integer_validator("width", width)
      self.__height= super().integer_validator("height", height)
    
    def __str__(self):
        """
        This method overides the other methods above it

        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
    
    def area(self):
        """
        This method returns the area of a rectangle
        """
        return self.__width * self.__height





     


