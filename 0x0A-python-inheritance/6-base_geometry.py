#!/usr/bin/python3
"""Module that contains the class BaseGeometry"""


class BaseGeometry():
    """Empy class"""

    def area(self):
        """Incomplete method"""

        raise Exception("area() is not implemented")

if __name__ == "__main__":
    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
