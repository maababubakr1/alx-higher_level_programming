#!/usr/bin/python3
"""Defines a base model class of classes """
import json


class Base:
    """Represents the base model class

    Represent the “base” of all other classes in this project

    Arg:
        - __nb_objects (int): the number of initiated bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new base

        Arg:
            - id (int): the identity of a new base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries

        Arg:
            - list_dictionaries (list): A list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Arg:
            - list_objs (list): A list of instances who inherits of Base
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string

        Arg:
            - json_string (str): A string representing a list of dictionaries
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set

        Arg:
            - **dictionary (dict): key/value pair of attributes
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Square":
                new = cls(1)
            else:
                new = cls(1, 1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances or an empty list"""

        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as f:
                list_dict = Base.from_json_string(f.read())
                return [cls.create(**d) for d in list_dict]
        except IOError:
            return []
