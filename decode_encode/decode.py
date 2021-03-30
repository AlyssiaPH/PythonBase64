"""Module encode

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

from decode_encode.helpers import *


def ascii_list_to_char(code_list):
    """
    Convert an int list to ascii list
    :param code_list:
    :type code_list: list
    :return a list of ascii:
    """
    for i in range(len(code_list)):
        code_list[i] = convert_ascii_to_char(code_list[i])

    return code_list


def add_zero_left_to_binary(binary_list, length=6):
    """
    Adds a 0 at left of every binary in the list and returns them
    :param binary_list: list of binaries
    :type binary_list: list
    :param length: length of intended string
    :type length: int
    :return: list of binaries with a 0 added at the beginning
    """
    for i in range(len(binary_list)):
        binary_list[i] = add_zero_at_left(str(binary_list[i]), length)
    return binary_list


def remove_first_zeros(binary_list):
    """
    remove 0 at left of every binary in the list and returns it
    :param binary_list: list of binaries
    :type binary_list: list
    :return: list of binaries without 0 at left
    """
    for i in range(len(binary_list)):
        try:
            binary_list[i] = binary_list[i][binary_list[i].index("1"):]
        except ValueError:
            pass

    return binary_list


def base_64_to_decimal(base_64_list):
    """
    Convert a char into a its base 64 index
    :param base_64_list: a list of string
    :type base_64_list: list
    :return: a list of base 64 decimal index
    """
    base_64 = get_base_64_string()
    for i in range(len(base_64_list)):
        base_64_list[i] = base_64.index(base_64_list[i])

    return base_64_list


def remove_char_to_match_multiplier_length(my_string, multiplier=8):
    """
    Remove enough char to have a string multiple of given multiplier
    :param my_string: a string to set
    :type my_string: str
    :param multiplier: string length multiplier
    :type multiplier: int
    :return: a string with a length exactly multiple of multiplier
    """
    return my_string[0:len(my_string) // multiplier * multiplier]


def run(user_input):
    if user_input == "":
        user_input = input("Type the string you would like to decode and press enter.")

    print("- Decode process starting -")

    step1 = remove_equals_chars(user_input)
    print(step1)

    step2 = string_to_char_list(step1)
    print(step2)

    step3 = base_64_to_decimal(step2)
    print(step3)

    step4 = ascii_list_to_binary(step3)
    print(step4)

    step5 = add_zero_left_to_binary(step4)
    print(step5)

    step6 = list_to_string(step5)
    print(step6)

    step7 = remove_char_to_match_multiplier_length(step6)
    print(step7)

    step8 = string_to_sized_strings_list(step7, 8)
    print(step8)

    step9 = remove_first_zeros(step8)
    print(step9)

    step10 = binary_list_to_decimal_list(step9)
    print(step10)

    step11 = ascii_list_to_char(step10)
    print(step11)

    final_step = list_to_string(step11)
    print(final_step)

    print("- Decode process ended -")

    return final_step
