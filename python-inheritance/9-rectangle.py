#!/usr/bin/python3
"""module of Rectangle, a child class of BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle inherited from BaseGeometry"""

    def __init__(self, width, height):
        """check width and height are positive integers"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculate the area of this rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """return the rectangle info"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
