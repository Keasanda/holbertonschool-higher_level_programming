#!/usr/bin/python3
"""write an object to a JSON text file"""


def save_to_json_file(my_obj, filename):
    """convert Python file to JSON file"""

    import json
    with open(filename, "w", encoding="utf-8") as j:
        j.write(json.dumps(my_obj))
