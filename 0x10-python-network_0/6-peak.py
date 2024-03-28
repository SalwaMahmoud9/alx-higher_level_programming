#!/usr/bin/python3
"""peak"""


def find_peak(list_of_integers):
    """find_peak"""
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size == 2:
        return max(list_of_integers)
    elif size == 1:
        return list_of_integers[0]

    mid = int(size / 2)
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
