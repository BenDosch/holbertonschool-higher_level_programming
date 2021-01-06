#!/usr/bin/python3
"""A module that contais the class square
"""


class Square:
    """A class with information about a square
    """

    def __init__(self, size=0, position=(0, 0)):
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
        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        """Propetry for position information
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for position
        """
        if type(vaule) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Method that returns the area of the square
        """
        return (self.__size * self.__size)

    def my_print(self):
        """Method that prints a square of #'s the size of the square
        precded by space or _'s according to position
        """
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print("_", end='')
            for k in range(self.__size):
                print("#", end='')
            print("")

if __name__ == "__main__":
    my_square_1 = Square(3)
    my_square_1.my_print()

    print("--")

    my_square_2 = Square(3, (1, 1))
    my_square_2.my_print()

    print("--")

    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()

    print("--")
