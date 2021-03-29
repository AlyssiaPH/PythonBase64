import re
import string


def string_to_list(my_string):
    """Returns the user string as a list
    :param my_string: user specified string:
    :return a list of string:"""
    return list(my_string)


def ascii_to_char(my_codes):
    """
    Convert string to ascii
    :param my_codes:
    :return a list of ascii:
    """
    for i in range(len(my_codes)):
        my_codes[i] = chr(my_codes[i])

    return my_codes


def ascii_to_binary(ascii_list):
    """
    Convert ascii list to binary list
    :param ascii_list: a list of ascii
    :return a list of binary:
    """
    for i in range(len(ascii_list)):
        ascii_list[i] = bin(ascii_list[i]).replace("0b", "")
    return ascii_list


def add_zero_to_binary(binary_list):
    """
    Adds a 0 on the left of every binary in the list and returns them
    :param binary_list: list of binaries
    :return : list of binaries with a 0 added at the beginning
    """
    for i in range(len(binary_list)):
        binary_list[i] = str(binary_list[i]).zfill(6)
    return binary_list


def remove_first_zeros(binary_list):
    """
    Adds a 0 on the left of every binary in the list and returns them
    :param binary_list: list of binaries
    :return : list of binaries with a 0 added at the beginning
    """
    for i in range(len(binary_list)):
        binary_list[i] = binary_list[i][1:]
    return binary_list


def binary_list_to_string(binary_list):
    """
    Convert and return a list of binaries to a single string
    :param binary_list: list of binaries
    :return: a string of every binaries combined
    """
    return "".join(binary_list)


def string_to_strings_list(string, n):
    """
    Convert a string to a list of strings
    :param string: string to be converted
    :param n: length of each string in the list that will be returned
    :return: a list of strings of n chars until there's not enough chars (last string will be of remaining chars length)
    """
    return [string[i:i+n] for i in range(0, len(string), n)]


def add_zeros_to_string_list(string_list):
    """
    Add 2 zeros on the right side of the last string in the list
    :param string_list: list of binaries
    :return: new list of strings where the last element has two 0 added on the right side
    """
    string_list[len(string_list) - 1] = string_list[len(string_list) - 1][0:4]
    return string_list


def binary_list_to_decimal_list(binary_list):
    """
    Convert a list of binaries to a list of decimals
    :param binary_list: a list of binaries
    :return: list of decimals
    """
    for i in range(len(binary_list)):
        binary_list[i] = int(binary_list[i], 2)
    return binary_list


def base_64_to_decimal(ascii_list):
    ascii = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"
    for i in range(len(ascii_list)):
        ascii_list[i] = ascii.index(ascii_list[i])
    return ascii_list


def remove_equals_chars(string):
    return string.replace('=', '')


def run(user_input):

    if user_input == "": user_input = input("Type the string you would like to decode and press enter.")
    print("- Decode process starting -")

    step1 = remove_equals_chars(user_input)
    print(step1)

    step2 = string_to_list(step1)
    print(step2)

    step3 = base_64_to_decimal(step2)
    print(step3)

    step4 = ascii_to_binary(step3)
    print(step4)

    step5 = add_zero_to_binary(step4)
    print(step5)

    step6 = add_zeros_to_string_list(step5)
    print(step6)

    step7 = binary_list_to_string(step6)
    print(step7)

    step8 = string_to_strings_list(step7, 8)
    print(step8)

    step9 = remove_first_zeros(step8)
    print(step9)

    step10 = binary_list_to_decimal_list(step9)
    print(step10)

    step11 = ascii_to_char(step10)
    print(step11)

    final_step = binary_list_to_string(step11)
    print(final_step)

    print("- Decode process ended -")

    return final_step