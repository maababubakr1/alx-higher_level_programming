#!/usr/bin/python3
""" Defines a class inherited checking function"""


def inherits_from(obj, a_class):
    """ checks if an object is an inherited instance of a class

    parameters:
    - obj (any): the object to check
    - a_class (type): the class to check the object with

    Return:
    True if the object is an instance of a class that
    inherited from the specified class
    otherwise False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
