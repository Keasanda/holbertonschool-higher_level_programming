#!/usr/bin/python3
"""return dict description with simple data struct for JSON serializat"""


def class_to_json(obj):
    """obj to json serialization"""

    return obj.__dict__
