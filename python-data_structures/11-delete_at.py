#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    for i in range(len(my_list)):
        if idx == i:
            del my_list[i]
    return my_list
