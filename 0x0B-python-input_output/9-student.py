#!/usr/bin/python3
"""Defines a class student"""


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """initialize a new student.

        args:
            - first_name (str): the first name of the student
            - last_name (str): the last name of the student
            - age (int): the age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation of a Student instance"""
        return self.__dict__
