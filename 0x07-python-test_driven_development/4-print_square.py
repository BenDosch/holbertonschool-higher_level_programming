#!/usr/bin/python3
"""A module that contains a function that prints a swaure of #'s
"""


def print_square(size):
    """Function that prints a squre of #'s

    Args:
        size (int): size of square

    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for range(0, size):
            print("{}".format("#" * size))
