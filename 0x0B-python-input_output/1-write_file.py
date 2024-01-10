#!/usr/bin/python3
# 1-write_file.py
"""write_file"""


def write_file(filename="", text=""):
    """write_file

    Args:
        filename (str): file name
        text (str): text
    Returns:
        write_file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
