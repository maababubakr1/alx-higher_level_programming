#!/usr/bin/python3r
""" Defines a lookup function for an object """


def lookup(obj):
    """Return a list of attributes and methods for an object"""
    return (dir(obj))
