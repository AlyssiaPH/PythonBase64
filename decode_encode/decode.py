"""Module encode

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

from decode_encode.helpers import *
import string


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
    Adds a 0 on the left of every binary in the list and returns them
    :param length: intended length of string
    :type length: int
    :param binary_list: list of binaries string
    :type binary_list: list
    :return : list of binaries with 0 added at the beginning if needed
    """
    for i in range(len(binary_list)):
        binary_list[i] = add_zero_at_left(str(binary_list[i]), length)
    return binary_list


#@todo remove all firsts zero
def remove_first_zeros(binary_list):
    """
    Adds a 0 on the left of every binary in the list and returns them
    :param binary_list: list of binaries
    :return : list of binaries with a 0 added at the beginning
    """
    for i in range(len(binary_list)):
        binary_list[i] = binary_list[i][1:]
    return binary_list


def add_zeros_to_string_list(string_list):
    """
    Add 2 zeros on the right side of the last string in the list
    :param string_list: list of binaries
    :return: new list of strings where the last element has two 0 added on the right side
    """
    string_list[len(string_list) - 1] = string_list[len(string_list) - 1][0:4]
    return string_list


def base_64_to_decimal(ascii_list):
    ascii = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"
    for i in range(len(ascii_list)):
        ascii_list[i] = ascii.index(ascii_list[i])
    return ascii_list


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

    step6 = add_zeros_to_string_list(step5)
    print(step6)

    step7 = list_to_string(step6)
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