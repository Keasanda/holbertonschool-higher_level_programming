#!/usr/bin/python3
"""add all arguments to a Python list and then save to a JSON file"""


import json
import sys
save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_fr_json = __import__('6-load_from_json_file').load_from_json_file
p_list = []
i = 0
for p_arg in sys.argv:
    if i > 0:
        p_list.append(p_arg)
    i += 1
try:
    with open("add_item.json", mode="x") as a_json:
        save_to_json(p_list, "add_item.json")
except:
    save_to_json(load_fr_json("add_item.json") + p_list, "add_item.json")
