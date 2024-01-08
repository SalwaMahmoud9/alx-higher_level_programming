#!/usr/bin/python3
# 2-is_same_class.py
"""is_same_class"""


def is_same_class(obj, a_class):
    """is_same_class

    Args:
        obj (any): object
        a_class (type): class
    Returns:
        If obj is instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
