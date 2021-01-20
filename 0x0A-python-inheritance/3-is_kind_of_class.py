#!/usr/bin/python3
""" Module that contains a function that compares objects to
see if they are instances of a class or its subclases"""


def is_kind_of_class(obj, a_class):
    """Checks if an objects is an instance of a class or of a subclass
    and returns True if the object is. Returns False on fail."""

    if type(obj) == a_class:
        return True
    elif issubclass(type(obj), a_class):
        return True
    else:
        return False

if __name__ == "__main__":
    a = 1
    if is_kind_of_class(a, int):
        print("{} comes from {}".format(a, int.__name__))
    if is_kind_of_class(a, float):
        print("{} comes from {}".format(a, float.__name__))
    if is_kind_of_class(a, object):
        print("{} comes from {}".format(a, object.__name__))
