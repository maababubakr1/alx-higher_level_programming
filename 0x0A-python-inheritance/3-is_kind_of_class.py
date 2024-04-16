#!/usr/bin/python3
""" Defines a calss and an inherited-class checking function"""


def is_kind_of_class(obj, a_class):
    """ckecks if  if the object is an instance or of a class that inherited from
    
    parameters:
    - obj (any): the object to check
    - a_class (type): the class to check the object with
    
    Return:
    True if the object is an instance of, or of a class that inherited from, the specified class
    otherwise False
    
    """
    if isinstance(obj, a_class):
        return True
    return False
