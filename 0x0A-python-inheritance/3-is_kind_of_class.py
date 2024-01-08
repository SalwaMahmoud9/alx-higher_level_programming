#!/usr/bin/python3
# 3-is_kind_of_class.py
"""is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class

    Args:
        obj (any): object
        a_class (type): class
    Returns:
        If obj is instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
