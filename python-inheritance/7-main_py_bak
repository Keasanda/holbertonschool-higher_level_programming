#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("{} {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("{} {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("{} {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("tooMany inputs", 2, 4)
except Exception as e:
    print("{} {}".format(e.__class__.__name__, e))

"""
try:
    bg.integer_validator(, 32)
except Exception as e:
    print("{} {}".format(e.__class__.__name__, e))
"""

try:
    bg.integer_validator("number")
except Exception as e:
    print("{} {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator()
except Exception as e:
    print("{} {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("name", [1, 2])
except Exception as e:
    print("{} {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("name", (1, 2))
except Exception as e:
    print("{} {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("name", {0: 1, 1: 3})
except Exception as e:
    print("{} {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("name", True)
except Exception as e:
    print("{} {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("name", None)
except Exception as e:
    print("{} {}".format(e.__class__.__name__, e))
