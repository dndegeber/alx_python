Square = __import__('0-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)  # This should raise an error
except Exception as e:
    print(e)

try:
    print(my_square.__size)  # This should raise an error
except Exception as e:
    print(e)
