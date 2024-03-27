#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """ Finds the peak in a list of integers """
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    mid = int(length / 2)
    li = list_of_integers

    if mid - 1 < 0 and mid + 1 >= length:
        return li[m]
    elif m - 1 < 0:
        return li[mid] if li[mid] > li[mid + 1] else li[mid + 1]
    elif m + 1 >= length:
        return li[mid] if li[mid] > li[mid - 1] else li[mid - 1]

    if li[mid - 1] < li[mid] > li[mid + 1]:
        return li[mid]

    if li[mid + 1] > li[mid - 1]:
        return find_peak(li[mid:])
    return find_peak(li[:mid])
