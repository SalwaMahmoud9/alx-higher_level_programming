#!/usr/bin/python3
# 10-student.py
"""Student"""


class Student:
    """student."""

    def __init__(self, first_name, last_name, age):
        """init

        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Student

        Args:
            attrs (list): (Optional)
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
