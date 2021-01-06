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

    def my_print(self):
        """Method that prints a square of #'s the size of the square
        """
        if self.__size == 0:
            print("")
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print("")

if __name__ == "__main__":
    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")
