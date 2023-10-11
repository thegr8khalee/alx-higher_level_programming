#!/usr/bin/python3
def  print_sorted_dictionary(a_dictionary):
    lists = list(a_dictionary.keys())
    lists.sort()
    for i in lists:
        print("{}: {}".format(i, a_dictionary.get(i)))
