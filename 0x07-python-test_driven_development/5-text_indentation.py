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

    text2 = text.strip()
    char = 0

    while char < (len(text2)):
        if text2[char] in ['.', '?', ':']:
            print("{}\n".format(text2[char]))
            while char < len(text2) - 1 and text2[char + 1] == " ":
                char += 1
            char += 1
        else:
            print(text2[char], end='')
            char += 1
