
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




     


