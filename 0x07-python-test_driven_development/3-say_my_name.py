#!/usr/bin/python3
""" Module containing a function that says your name
"""


def say_my_name(first_name, last_name=""):
    """ function that prints, 'my name is' followed by a first and last name

    Args:
        first_name (str): Individual's name
        last_name (str): Family's name

    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
