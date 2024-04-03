#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """initialize a new square

        Args:
        size (int): The size of new Square
        """
        self.size = size

    @property
    def size(self):
        """get/set the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the current area of the square"""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """ define == comparaison"""
        return self.area() == other.area()

    def __ne__(self, other):
        """ define 1= comparaison"""
        return self.area() != other.area()

    def __It__(self, other):
        """ define < comparaison"""
        return self.area() < other.area()

    def __le__(self, other):
        """ define <= comparaison"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """ define > comparaison"""
        return self.area() > other.area()

    def __ge__(self, other):
        """ define >= comparaison"""
        return self.area() >= other.area()
