#!/usr/bin/python3
"""Defines a json to object converting function"""
import json


def from_json_string(my_str):
    """returns an object represented by a JSON string"""
    return json.loads(my_str)
