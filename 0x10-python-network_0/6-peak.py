#!/usr/bin/python3
<<<<<<< HEAD
"""function that finds a peak in a list of unsorted integers."""
=======
"""Defines a peak-finding algorithm."""

>>>>>>> 895cd0d1c5906d3594ab13596466e247421161fc

def find_peak(list_of_integers):
    """ Finds the peak in a list of integers """
    if list_of_integers == []:
        return None
<<<<<<< HEAD
    elif length == 1:
        return list_of_integers[0]
    else:
        try:
            li = list_of_integers
            if li[mid] > li[mid - 1] and li[mid] > li[mid + 1]:
                return li[mid]
            elif li[mid - 1] > li[mid] and li[mid - 1] > li[mid + 1]
                find_peak(li[:mid])
            elif li[mid + 1] > li[mid] and li[mid + 1] > li[mid -1]
                find_peak(li[mid + 1:])
        except IndexError:
            pass
            
=======

    length = len(list_of_integers)
    mid = int(length / 2)
    li = list_of_integers

    if mid - 1 < 0 and mid + 1 >= length:
        return li[m]
    elif mid - 1 < 0:
        return li[mid] if li[mid] > li[mid + 1] else li[mid + 1]
    elif mid + 1 >= length:
        return li[mid] if li[mid] > li[mid - 1] else li[mid - 1]

    if li[mid - 1] < li[mid] > li[mid + 1]:
        return li[mid]

    if li[mid + 1] > li[mid - 1]:
        return find_peak(li[mid:])
    return find_peak(li[:mid])
>>>>>>> 895cd0d1c5906d3594ab13596466e247421161fc
