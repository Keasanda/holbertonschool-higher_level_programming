#!/usr/bin/python3
"""function return True if object is instance of the class, otherwise False"""


def is_same_class(obj, a_class):
    """return True or False"""

    if type(obj) is a_class:
        return True
    else:
        return False
