#!/usr/bin/python3
"""Module: 4-from_json_string
returns an object (Python data structure)
represented by a JSON string
"""


import json


def from_json_string(my_str):
    """ function that returns an object
    (Python data structure) represented by a JSON string

    Args:
    - my_str: the argument to be deserialized
    """

    return json.loads(my_str)
