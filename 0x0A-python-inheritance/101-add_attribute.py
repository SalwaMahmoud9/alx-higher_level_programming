#!/usr/bin/python3
# 101-add_attribute.py
"""add_attribute"""


def add_attribute(obj, att, value):
    """add_attribute

    Args:
        obj (any): object
        att (str): attribute
        value (any): value
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
