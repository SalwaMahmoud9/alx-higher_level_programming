#!/usr/bin/python3
# 2-append_write.py
"""append_write"""


def append_write(filename="", text=""):
    """append_write

    Args:
        filename (str): file name
        text (str): text
    Returns:
        append_write
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
