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
