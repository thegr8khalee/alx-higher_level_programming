#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_one = my_list.copy()
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            new_one[i] = 1
        else:
            new_one[i] = 0
    return new_one
