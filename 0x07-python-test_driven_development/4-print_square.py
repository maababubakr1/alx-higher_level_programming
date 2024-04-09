#!/usr/bin/python3
""" Defines a function that prints a square with the character #."""


def print_square(size):
    """
    A function that prints a square with the character #

    Parameter:
        - size(int): The Height/Width of the square
    Raise:
        TypeError: if size is not an int
        ValueError: if size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
