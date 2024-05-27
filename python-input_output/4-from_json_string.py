#!/usr/bin/python3
"""return an Python data structure obj represented by a JSON string"""


def from_json_string(my_str):
    """convert from JSON to Python"""

    import json
    return json.loads(my_str)
