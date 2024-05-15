#!/usr/bin/python3
"""
This class define a square
"""


class Square:
    """
    This class represents a square.

    Attributes:
        Size: size of square.
    """

    def __init__(self, size=0):
        """
        Thi method initializes a Square instance
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
