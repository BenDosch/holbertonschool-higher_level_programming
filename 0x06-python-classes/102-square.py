#!/usr/bin/python3
"""A module that contais the class square
"""


class Square:
    """A class with information about a square
    """

    def __init__(self, size=0):
        """initialization of function
        Args:
            size (int, optional): Size of the square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """Property that returns size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Method that returns the area of the square
        """
        return (self.__size * self.__size)


if __name__ == "__main__":
    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)
