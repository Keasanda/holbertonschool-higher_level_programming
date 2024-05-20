#!/usr/bin/python3
"""if the object is an inst of object or class return True, otherwise False"""


def is_kind_of_class(obj, a_class):
    """return True or False"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
