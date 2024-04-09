#!/usr/bin/python3
""" Defines a text-indentation function """


def text_indentation(text):
    """ function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Parameter:
        text(str): the text to be printed

    Raise:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
