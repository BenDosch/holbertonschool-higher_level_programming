#!/usr/bin/python3
"""Module contians a function that returns a list of avalible atributes and
methods of an object"""


def lookup(obj):
    """ returns a list of avalible atributes and methods of an object

    Args:
        obj (any): object to get list from """

    return dir(obj)


if __name__ == "__main__":
    class MyClass1(object):
        pass

    class MyClass2(object):
        my_attr1 = 3

    def my_meth(self):
        pass

    print(lookup(MyClass1))
    print(lookup(MyClass2))
    print(lookup(int))
