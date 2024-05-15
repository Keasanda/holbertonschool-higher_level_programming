#!/usr/bin/python3
"""
    This class represent a square
"""


class Square:
    """
    This class creates a square with size and position
    """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        This method get size of a side de square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This method sets the size of a side the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        This method get position the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        This method sets the position square
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        This method calculate area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        This Public method that print square with "#"
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for a in range(self.__size):
                print(" " * self.__position[0], end="")
                for b in range(self.__size):
                    print("#", end="")
                print()
