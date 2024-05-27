#!/usr/bin/python3
"""a function that creates an Object from a JSON file"""


def load_from_json_file(filename):
    """from JSON to Python file"""

    import json
    with open(filename, encoding="utf-8") as p_file:
        return json.load(p_file)
