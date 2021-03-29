"""Module encode

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

import re
import string


# step 1
def string_to_char_list(my_string):
    """
    Return a string as a list of char (string with len equal 1)
    :param my_string: a string to convert as list of char
    :type my_string: str
    :return: a list of char
    """
    return list(my_string)


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


def char_to_ascii_code(char):
    """
    Convert a char to its ascii code
    :param char: a char (a string of length equal 1 )
    :type char: str
    :return: an ascii code
    """
    return ord(char)


# step 3
def ascii_list_to_binary(ascii_list):
    """
    Convert each ascii code in list to its binary value
    :param ascii_list: a list of ascii code
    :type ascii_list: list
    :return: a list of binary
    """
    for i in range(len(ascii_list)):
        ascii_list[i] = ascii_to_binary(ascii_list[i])
    return ascii_list


def ascii_to_binary(ascii_code):
    """
    Convert an ascii code to binary
    :param ascii_code: an ascii code
    :type ascii_code: int
    :return: a binary string
    """
    return bin(ascii_code).replace("0b", "")


# step 4
def add_zero_left_to_binary_list(binary_list):
    """
    Adds a 0 at left of every binary in the list and returns them
    :param binary_list: list of binaries
    :type binary_list: list
    :return: list of binaries with a 0 added at the beginning
    """
    for i in range(len(binary_list)):
        binary_list[i] = add_zero_at_left(binary_list[i], 8)
    return binary_list


def add_zero_at_left(my_string, length):
    """
    add enough 0 at left of a string to have string length equal to given length
    :param my_string: a string
    :type my_string: str
    :param length: intended string length
    :type length: int
    """
    return str(my_string).zfill(length)


# step 5 & 10
def list_to_string(my_list):
    """
    Convert and return a list as a single string
    :param my_list: list of string
    :type my_list: list
    :return: a string of each list elements combined
    """
    return "".join(my_list)


# step 6
def string_to_sized_strings_list(my_string, length):
    """
    Convert a string to a list of sized strings.
    these strings has n chars until there's not enough chars
    (last string will be of remaining chars length)
    :param my_string: string to be converted
    :type my_string: str
    :param length: length of each string
    :type length: int
    :return: a string list
    """
    return [my_string[i:i + length] for i in range(0, len(my_string), length)]


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
    string_list[len(string_list) - 1] = add_zero_to_right( string_list[len(string_list) - 1], length)
    return string_list


def add_zero_to_right(my_string, length):
    """
    Add enough zeros at right side of a string to equal length
    :param length: string length
    :type length: int
    :param my_string: a string
    :type my_string: str
    :return: new list of strings where the last element has two 0 added on the right side
    """
    return my_string.ljust(length, '0')


# step 8
def binary_list_to_decimal_list(binary_list):
    """
    Convert a list of binaries to a list of decimals
    :param binary_list: a list of binaries
    :type binary_list: list
    :return: list of decimals
    """
    for i in range(len(binary_list)):
        binary_list[i] = binary_to_decimal(binary_list[i])
    return binary_list


def binary_to_decimal(integer):
    """
    Convert a binary to decimal
    :param integer: a string containing a binary value
    :type integer: str
    :return: a decimal value
    """
    return int(integer, 2)


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


def get_base_64_string():
    """
    Get all character from base 64
    :return: a string
    """
    return string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"


def convert_decimal_to_base_64(integer):
    """
    Convert an int to its corresponding char in base 64
    :param integer: an int between 0 to 63
    :type integer: int
    :return: the corresponding base 64 char at index
    """
    return get_base_64_string()[integer]


# step 11
def fill_string_to_match_multiplier_length(my_string, multiplier=4):
    """
    Adds enough '=' characters to have a string length multiple of multiplier value
    :param my_string: the string that will be filled
    :type my_string: str
    :param multiplier: the multiplier value of string length
    :type multiplier: int
    :return: a new string with '=' chars added if needed to have a length multiplier of given multiplier
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
    print (final_step)

    print("- Encode process ended -")

    return final_step

