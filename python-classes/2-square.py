#!/usr/bin/python3
"""square"""


class Square:
    """square"""

    def __init__(self, size=0):
        """square

        args:
            self: instance
            size: size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
