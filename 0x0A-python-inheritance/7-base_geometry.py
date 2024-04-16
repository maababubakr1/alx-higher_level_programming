#!/usr/bin/python3
"""Defines an empty class"""


class BaseGeometry:
    """A base geometry"""
    def area(self):
        """no implementation"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate a parameter (as an integer)

        parameters:
        - name (str): the name of the parameter
        - value (int): the parameter to be validated

        Raises:
        - TypeError if value is not an int
        - ValueError if value <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
