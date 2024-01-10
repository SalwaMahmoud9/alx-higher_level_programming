#!/usr/bin/python3
# 100-append_after.py
"""append_after"""


def append_after(filename="", search_string="", new_string=""):
    """append_after

    Args:
        filename (str): file name
        search_string (str): string to search
        new_string (str): string to insert
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
