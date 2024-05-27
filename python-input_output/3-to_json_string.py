#!/usr/bin/python3
"""a function returns the JSON representation of an object"""


def to_json_string(my_obj):
    """return the JSON format of an object(string)"""

    import json
    return json.dumps(my_obj)
