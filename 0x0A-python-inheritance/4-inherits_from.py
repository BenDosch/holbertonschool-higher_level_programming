#!/usr/bin/python3
"""Module containing a function that checks if an ojcect is of a subcalss
of a specified class"""


def inherits_from(obj, a_class):
    """Function that checks if  if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class """

    if issubclass(type(obj), a_class) and not type(obj) == a_class:
        return True
    else:
        return False

if __name__ == "__main__":
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
