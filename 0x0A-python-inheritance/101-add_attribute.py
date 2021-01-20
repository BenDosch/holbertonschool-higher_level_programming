#!/usr/bin/python3
"""Module that contains a function which adds a new atribute to an object if
it is possible."""


def add_attribute(obj, a_name, a_value):
    """Function that adds a new attribute to an object if its possible.


    Args:
        obj (object):
        a_name (str): name of attribue to add
        a_value (any): value of attribute to add

    """
    if "__dict__" in dir(obj):
        setattr(obj, a_name, a_value)
    else:
        raise TypeError("can't add new attribute")
