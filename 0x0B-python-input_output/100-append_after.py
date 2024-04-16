#!/usr/bin/python3
"""Define a text file line inserting function"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file, after a specific string

    args:
        - filename (str): the name of the file
        - search_string (str): the string to search
        - new_string (str): the string to insert
    """
    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
