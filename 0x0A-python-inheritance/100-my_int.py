#!/usr/bin/python3
"""Module that contains the class MyInt, a subclass of int"""


class MyInt(int):
    """int with == and != reversed"""

    def __eq__(self, other):
        """reverse of equals"""

        return super().__ne__(other)

    def __ne__(self, other):
        """revers of not equal"""

        return super().__eq__(other)

if __name__ == "__main__":
    my_i = MyInt(3)
    print(my_i)
    print("--")
    print(my_i == 3)
    print("--")
    print(my_i != 3)
