#!/usr/bin/python3
"""Module that contains the class Rectangle
"""


class Rectangle():
    """Class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initilization method for Rectangle.

        Args:
            width (int): Optional: must be >= 0
            heigth (int): Optional: must be >= 0

        """

        self.width = width
        self.height = height


    @property
    def width(self):
        """Method that returns the value of width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width.

        Args:
            value (int): must be greater than or equal to 0

        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Method that returns the value of height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height.

        Args:
            value (int): must be greater than or equal to 0

        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


    def area(self):
        """Method that returns the area of the Rectangle."""

        return (self.width * self.height)

    def perimeter(self):
        """Method that returns the perimiter of the Rectangle."""

        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (2 * (self.width + self.height))


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(),
                                            my_rectangle.perimeter()))

    print("--")

    my_rectangle.width = 10
    my_rectangle.height = 3
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(),
                                            my_rectangle.perimeter()))
