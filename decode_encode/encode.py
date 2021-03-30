"""Module encode

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

from decode_encode.helpers import *


# step 2
def char_list_to_ascii_code(char_list):
    """
    Convert each char in list to its ascii code
    :param char_list: a list of char
    :type char_list: list
    :return: a list of ascii
    """
    for i in range(len(char_list)):
        char_list[i] = char_to_ascii_code(char_list[i])

    return char_list


# step 4
def add_zero_left_to_binary_list(binary_list, length=8):
    """
    Adds a 0 at left of every binary in the list and returns them
    :param binary_list: list of binaries
    :type binary_list: list
    :param length: length of intended string
    :type length: int
    :return: list of binaries with a 0 added at the beginning
    """
    for i in range(len(binary_list)):
        binary_list[i] = add_zero_at_left(binary_list[i], length)
    return binary_list


# step 7
def add_zero_right_to_string_list(string_list, length=6):
    """
    Add enough zeros at right side of the last string in the list to equal length
    (6 char by default)
    :param length: string length
    :type length: int
    :param string_list: list of binaries
    :type string_list: list
    :return: new list of strings where the last element is completed with 0 at right side
    """
    string_list[len(string_list) - 1] = add_zero_at_right(string_list[len(string_list) - 1], length)
    return string_list


# step 9
def decimal_to_base_64_char(decimal_list):
    """
    Convert a list of int to their corresponding Base64 char
    :param decimal_list: list of int
    :return: list of base 64 elements
    """
    for i in range(len(decimal_list)):
        decimal_list[i] = convert_decimal_to_base_64(decimal_list[i])
    return decimal_list


# step 11
def fill_string_to_match_multiplier_length(my_string, multiplier=4):
    """
    Adds enough "=" characters to have a string length multiple of multiplier value
    :param my_string: the string that will be filled
    :type my_string: str
    :param multiplier: the multiplier value of string length
    :type multiplier: int
    :return: a new string with "=" chars added if needed to have a length multiplier of given multiplier
    """
    return my_string + "=" * (multiplier - len(my_string) % multiplier)


def run(user_input):
    """
    Main function of this module, used to encode a string
    :param user_input: a string given by user
    :type user_input: str
    :return: a string encoded
    """

    if user_input == "":
        user_input = input("Type the string you would like to encode and press enter.")

    print("- Encode process starting -")

    step1 = string_to_char_list(user_input)
    print(step1)

    step2 = char_list_to_ascii_code(step1)
    print(step2)

    step3 = ascii_list_to_binary(step2)
    print(step3)

    step4 = add_zero_left_to_binary_list(step3)
    print(step4)

    step5 = list_to_string(step4)
    print(step5)

    step6 = string_to_sized_strings_list(step5, 6)
    print(step6)

    step7 = add_zero_right_to_string_list(step6)
    print(step7)

    step8 = binary_list_to_decimal_list(step7)
    print(step8)

    step9 = decimal_to_base_64_char(step8)
    print(step9)

    step10 = list_to_string(step9)
    print(step10)

    final_step = fill_string_to_match_multiplier_length(step10)
    print(final_step)

    print("- Encode process ended -")

    return final_step

