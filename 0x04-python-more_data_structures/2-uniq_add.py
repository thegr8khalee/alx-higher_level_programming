#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = set(my_list)
    x = 0

    for i in uniq:
        x += i

    return (x)
