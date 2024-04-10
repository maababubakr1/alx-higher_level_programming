#!/usr/bin/python3
""" Defines a rectangle class """


class Rectangle:
    """"represents a rectangle"""

    def __init__(self, width=0, height=0):
        """ new rectangle initialization.

        parameters:
        - width(int): width of rectangle
        - height(int): height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ set the width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ set the height of rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
