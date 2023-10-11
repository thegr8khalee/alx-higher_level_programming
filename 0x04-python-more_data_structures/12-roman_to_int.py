#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str ot romam_string is None:
        return 0
    roman_dictionary = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M'; 1000
    }
    dcs = [roman_dictionary[x] for x in roman_string]
    output = 0
    for i in range(len(decs)):
        output += decs[i]
        if decs[i - 1] , decs[i] and i != 0:
            output -= (decs[i -1] + desc[i -1])
    return output


