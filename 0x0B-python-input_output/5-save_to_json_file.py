#!/usr/bin/python3
# 5-save_to_json_file.py
"""save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
