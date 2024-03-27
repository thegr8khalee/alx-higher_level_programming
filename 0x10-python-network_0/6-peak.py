#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers."""

def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers."""
    length = len(list_of_integers)
    mid = length // 2
    if length == 0:
        return None
    elif length == 1:
        return list_of_integers[0]
    else:
        li = list_of_integers
        if li[mid] > li[mid - 1] and li[mid] > li[mid + 1]:
            return li[mid]
        elif li[mid - 1] > li[mid] and li[mid - 1] > li[mid + 1]:
            find_peak(li[:mid])
        elif li[mid + 1] > li[mid] and li[mid + 1] > li[mid -1]:
            find_peak(li[mid + 1:])
            
