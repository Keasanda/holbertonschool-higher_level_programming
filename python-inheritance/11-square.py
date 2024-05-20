#!/usr/bin/python3
"""class Square, inherited from class Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square, child of Rectangle, child of child of BaseGeometry"""

    def __init__(self, size):
        """initialize class with size"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """area method must be implemented"""
        return self.__size * self.__size

    def __str__(self):
        """return the square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
