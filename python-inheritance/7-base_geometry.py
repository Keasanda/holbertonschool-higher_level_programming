#!/usr/bin/python3
"""module of BaseGeometry"""


class BaseGeometry:
    """module of BaseGeometry"""

    def area(self):
        """empty area() function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate input value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
