#!/usr/bin/python3
"""a class Student"""


class Student:
    """a class of Student"""

    def __init__(self, first_name, last_name, age):
        """instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieve dict representation"""
        cp_dict = self.__dict__.copy()
        l_item = {}
        if type(attrs) == list:
            for i in cp_dict:
                for j in range(len(attrs)):
                    if i == attrs[j]:
                        l_item[i] = cp_dict[i]
            return l_item
        return self.__dict__
