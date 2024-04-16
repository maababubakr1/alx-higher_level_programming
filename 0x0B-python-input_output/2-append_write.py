#!/usr/bin/python3
"""Defines a file appending function"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)

    args:
        - filename (str): the file to append to
        - text (str): the text to be appended

    Return:
        the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
