#!/usr/bin/python3
def roman_to_int(roman_string):

    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    result = 0
    prev_val = 0

    for numeral in reversed(roman_string):
        current_val = roman_n.get(numeral, 0)

        if current_val >= prev_val:
            result += current_val
        else:
            result -= current_val

        prev_val = current_val

    return result
