#!/usr/bin/python3
"""a class MyList inherits from list"""


class MyList(list):
    """a subclass of list"""

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
