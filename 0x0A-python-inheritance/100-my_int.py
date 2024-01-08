#!/usr/bin/python3
# 100-my_int.py
"""MyInt"""


class c(int):
    """MyInt"""

    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
