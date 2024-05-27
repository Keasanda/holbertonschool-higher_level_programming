#!/usr/bin/python3
"""appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """appends text at filename and returns len of text"""

    with open(filename, "a", encoding="utf-8") as a_file:
        return a_file.write(text)
