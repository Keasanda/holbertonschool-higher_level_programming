#!/usr/bin/python3
"""
This module print a text
"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines after characters . , ? :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    print(text)
