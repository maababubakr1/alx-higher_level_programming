#!/usr/bin/python3
"""
A function that adds 2 integers.

 Floats are typecasted to integers before addition.
"""


def add_integer(a, b=98):
    """
    Function that adds two int values.
    Parameters:
        - a(int or float): first parameter
        - b(int or float): second parameter
        - Returns: an integer, the addition of a and b.

    Raises:
        TypeError: if either a, b is non-int and non-float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
