#!/usr/bin/python3
# 7-base_geometry.py
"""BaseGeometry"""


class BaseGeometry:
    """BaseGeometry"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """BaseGeometry

        Args:
            name (str): name
            value (int): value
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
