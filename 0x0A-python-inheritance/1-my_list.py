#!/usr/bin/python3
""" Define an inherited list class Mylist"""


class MyList(list):
    """ Implement ascending sorting for list built-in class """

    def print_sorted(self):
        """ Print the list in ascending sorted order """
        print(sorted(self))
