#!/usr/bin/python3
"""square"""


class Square:
    """square"""

    def __init__(self, size=0):
        """square

        args:
            size: size of square
            self: instance
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area"""
        return self.__size * self.__size
