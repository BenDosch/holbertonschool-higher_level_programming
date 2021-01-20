#!/usr/bin/python3
""" Module that contains a function that compares objects to
see if they are instances of a specific class """


def is_same_class(obj, a_class):
    """Checks if an objects is an instance of a class and returns True if
    the object is. Returns False on fail."""

    if type(obj) is a_class:
        return True
    else:
        return False

if __name__ == "__main__":
    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
