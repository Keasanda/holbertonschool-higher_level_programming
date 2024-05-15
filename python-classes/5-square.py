#!/usr/bin/python3
"""square"""


class Square:
    """square"""

    def __init__(self, size=0):
        """square

        args:
            self: instance
            size: square size
        """
        self.__size = size

    @property
    def size(self):
        """current square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set square size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area"""
        return self.__size * self.__size

    def my_print(self):
        """print square"""
        for i in range(self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
