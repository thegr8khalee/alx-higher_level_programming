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
        try:
            li = list_of_integers
            if (li[mid] >= li[mid - 1] if mid - 1 >= 0 else True) and \
                (li[mid] >= li[mid + 1] if mid + 1 < length else True):
                    return li[mid]
            elif li[mid - 1] > li[mid]:
                return find_peak(li[:mid])
            else:
                return find_peak(li[mid + 1:])
        except IndexError:
            pass
            