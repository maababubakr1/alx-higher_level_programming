#!/usr/bin/python3
"""Defines a json fike reading function"""
import json


def load_from_json_file(filename):
    """creates an Object from a JSON file"""
    with open(filename) as f:
        return json.load(f)
