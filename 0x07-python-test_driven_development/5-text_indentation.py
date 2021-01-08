#!/usr/bin/python3
"""Module that prints a text with 2 newlines after some characters
"""


def text_indentation(text):
    """Function that prints a text with 2 new lines after each of
    these characters: . ? and :

    Args:
        text (str): text to print modified version of

    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for char in text:
        if char in ['.', '?', ':']:
            print("{}\n".format(char))
        else:
            print(char, end='')
