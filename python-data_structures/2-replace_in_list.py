#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    for i in range(0, idx + 1):
        if i == idx:
            my_list[i] = element
    return my_list
