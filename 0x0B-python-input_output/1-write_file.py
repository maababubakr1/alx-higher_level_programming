#!/usr/bin/python3
"""defines a text file writing function"""


def write_file(filename="", text=""):
    """write a string to  text file

    parameters:
    - filename (str): the name of the file to write on
    - text (str): the text to be written on a file

    Returns the number of lines in a text file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
