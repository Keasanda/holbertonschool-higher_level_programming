#!/usr/bin/python3
for i in range(0, 10):
    for a in range(i + 1, 10):
        if i != a:
            print("{}{}".format(i, a), end=", " if i != 8 or a != 9 else '\n')
