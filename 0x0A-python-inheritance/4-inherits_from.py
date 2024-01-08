#!/usr/bin/python3
# 4-inherits_from.py
"""inherits_from"""


def inherits_from(obj, a_class):
    """inherits_from

    Args:
        obj (any): object
        a_class (type): class
    Returns:
        If obj is inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
