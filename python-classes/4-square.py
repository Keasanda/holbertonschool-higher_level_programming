#!/usr/bin/python3
"""
This class define a square
"""


class Square:
    """
    This class define a square.
    Attributes:
        size: size of square.
    """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        This public instance method calculate the square area
        """
        return self.__size ** 2
