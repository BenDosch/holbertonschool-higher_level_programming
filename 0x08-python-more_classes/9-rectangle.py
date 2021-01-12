#!/usr/bin/python3
"""Module that contains the class Rectangle
"""


class Rectangle():
    """Class that defines a rectangle

    Atributes:
        number_of_instances (int): tracks the number of
                                   instances of the Rectangle class
        print_symbol (any): symbol used to create a visual of Rectangle

    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initilization method for Rectangle.

        Args:
            width (int): Optional: must be >= 0
            heigth (int): Optional: must be >= 0

        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Method that returns readable form of Rectangle made of symbols"""

        if self.perimeter() == 0:
            return ""
        else:
            return (((("{}".format(self.print_symbol)) * self.width + "\n") *
                    (self.height) + ("{}".format(self.print_symbol) *
                    self.width)))

    def __repr__(self):
        """Method that returns a string representation of the Rectangle
            to be able to recreate a new instance"""

        return 'Rectangle(%s, %s)' % (self.width, self.height)

    def __del__(self):
        """Destructor method for Rectangle"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares 2 Rectangle objects and returns
        the one with the biger area"""

        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Method that creates a square instance of a Rectangle object"""

        return cls(size, size)

if __name__ == "__main__":
    my_square = Rectangle.square(5)
    print("Area: {} - Perimeter: {}".format(my_square.area(),
                                            my_square.perimeter()))
    print(my_square)
