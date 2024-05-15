#!/usr/bin/python3
def search_replace(my_list, search, replace):

    newlist = my_list.copy()

    for a in range(len(newlist)):
        if newlist[a] == search:
            newlist[a] = replace
    return newlist
