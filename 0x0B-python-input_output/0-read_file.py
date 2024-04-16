#!/usr/bin/python3
"""Defines a text file reading function"""


def read_file(filename=""):
    """print the content of a file to stdout"""
    with open(filename, encoding="utf-8") as fi:
        print(fi.read(), end="")
