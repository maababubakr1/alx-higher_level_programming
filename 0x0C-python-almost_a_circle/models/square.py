#!/usr/bin/python3
""""Defines a square child class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new square

        Args:
            - size (int): The size of he new square
            - x (int): the x coordinate of the new square
            - y (int): the y coordinate of the new square
            - id (int): the identity of a new square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """"Get/Set the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the square

        Args:
            - *args (ints): New values of attribute:
                - 1st argument should be the id attribute
                - 2nd argument should be the size attribute
                - 3rd argument should be the x attribute
                - 4th argument should be the y attribute
            - **kwargs (dict): new key/value pairs
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation pf square"""
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
        }

    def __str__(self):
        """Return a representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
