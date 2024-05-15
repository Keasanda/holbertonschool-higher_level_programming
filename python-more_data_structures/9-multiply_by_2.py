#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdictionary = {}
    for i, value in a_dictionary.items():
        newdictionary[i] = value * 2
    return newdictionary
