#!/usr/bin/python3
""" Defines a check of objects within a class function"""


def is_same_class(obj, a_class):
    """checks if the object is exactly an instance of the specified class

    parameters:
    - obj (any): the object to check
    - a_class (type): the class to check the object with

    Return:
        True if the object is exactly an instance of the specified class.
        otherwise False

    """
    if type(obj) == a_class:
        return True
    return False
