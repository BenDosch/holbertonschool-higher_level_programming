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


if __name__ == "__main__":
    class MyClass():
        pass

    mc = MyClass()
    add_attribute(mc, "name", "John")
    print(mc.name)

    try:
        a = "My String"
        add_attribute(a, "name", "Bob")
        print(a.name)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
