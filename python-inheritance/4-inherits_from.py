#!/usr/bin/python3
"""return True if the instance is inherited, otherwise return False"""


def inherits_from(obj, a_class):
    """check if the instance is inherited"""

    if type(obj) is a_class:
        return False
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
