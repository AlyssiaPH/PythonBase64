"""Module 

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

import string


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


#region list operation

def string_to_char_list(my_string):
    """
    Return a string as a list of char (string with len equal 1)
    :param my_string: a string to convert as list of char
    :type my_string: str
    :return: a list of char
    """
    return list(my_string)


def list_to_string(my_list):
    """
    Convert and return a list as a single string
    :param my_list: list of string
    :type my_list: list
    :return: a string of each list elements combined
    """
    return "".join(my_list)


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

#endregion


#region simple convertion

def ascii_to_binary(ascii_code):
    """
    Convert an ascii code to binary
    :param ascii_code: an ascii code
    :type ascii_code: int
    :return: a binary string
    """
    return bin(ascii_code).replace("0b", "")


def char_to_ascii_code(char):
    """
    Convert a char to its ascii code
    :param char: a char (a string of length equal 1 )
    :type char: str
    :return: an ascii code
    """
    return ord(char)


def convert_ascii_to_char(integer):
    """
    Convert an int to an ascii char
    :param integer: an int
    :type integer: int
    :return: a char
    """
    return chr(integer)


def binary_to_decimal(integer):
    """
    Convert a binary to decimal
    :param integer: a string containing a binary value
    :type integer: str
    :return: a decimal value
    """
    return int(integer, 2)


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

#endregion


def add_zero_at_left(my_string, length):
    """
    add enough 0 at left of a string to have string length equal to given length
    :param my_string: a string
    :type my_string: str
    :param length: intended string length
    :type length: int
    """
    return str(my_string).zfill(length)


def add_zero_at_right(my_string, length):
    """
    Add enough zeros at right side of a string to equal length
    :param length: string length
    :type length: int
    :param my_string: a string
    :type my_string: str
    :return: new list of strings where the last element has two 0 added on the right side
    """
    return my_string.ljust(length, '0')


def remove_equals_chars(my_string):
    """
    Remove all '=' char in a string
    :param my_string: a string
    :return: a string without "=" char
    """
    return my_string.replace('=', '')


