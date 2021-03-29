import re
import string
import decode_encode.decode


# step 1
def string_to_list(my_string):
    """Returns the user string as a list
    :param my_string: user specified string:
    :return a list of string:"""
    return list(my_string)


# step 2
def code_to_ascii(my_codes):
    """
    Convert string to ascii
    :param my_codes:
    :return a list of ascii:
    """
    for i in range(len(my_codes)):
        my_codes[i] = ord(my_codes[i])

    return my_codes


# step 3
def ascii_to_binary(ascii_list):
    """
    Convert ascii list to binary list
    :param ascii_list: a list of ascii
    :return a list of binary:
    """
    for i in range(len(ascii_list)):
        ascii_list[i] = bin(ascii_list[i]).replace("0b", "")
    return ascii_list


# step 4
def add_zero_to_binary(binary_list):
    """
    Adds a 0 on the left of every binary in the list and returns them
    :param binary_list: list of binaries
    :return : list of binaries with a 0 added at the beginning
    """
    for i in range(len(binary_list)):
        binary_list[i] = str(binary_list[i]).zfill(8)
    return binary_list


# step 5 & 10
def binary_list_to_string(binary_list):
    """
    Convert and return a list of binaries to a single string
    :param binary_list: list of binaries
    :return: a string of every binaries combined
    """
    return "".join(binary_list)


# step 6
def string_to_strings_list(string, n):
    """
    Convert a string to a list of strings
    :param string: string to be converted
    :param n: length of each string in the list that will be returned
    :return: a list of strings of n chars until there's not enough chars (last string will be of remaining chars length)
    """
    return [string[i:i+n] for i in range(0, len(string), n)]


# step 7
def add_zeros_to_string_list(string_list):
    """
    Add 2 zeros on the right side of the last string in the list
    :param string_list: list of binaries
    :return: new list of strings where the last element has two 0 added on the right side
    """
    string_list[len(string_list) - 1] = string_list[len(string_list) - 1].ljust(6, '0')
    return string_list


# step 8
def binary_list_to_decimal_list(binary_list):
    """
    Convert a list of binaries to a list of decimals
    :param binary_list: a list of binaries
    :return: list of decimals
    """
    for i in range(len(binary_list)):
        binary_list[i] = int(binary_list[i], 2)
    return binary_list


# step 9
def ascii_to_base_64(ascii_list):
    """
    Convert a list of ascii codes to their corresponding Base64 char
    :param ascii_list: list of ascii codes
    :return: list of base 64 elements
    """
    ascii = string.ascii_uppercase + string.ascii_lowercase + "0123456789+/"
    for i in range(len(ascii_list)):
        ascii_list[i] = ascii[ascii_list[i]]
    return ascii_list


# step 11
def fill_string_to_match_multiplier_length(string, n):
    """
    Adds '=' characters while the string length is not equal to a multiplier of the n argument
    :param string: the string that will be checked
    :param n: the length of the returned string has to be a multiplier of n
    :return: a new string with '=' chars added if needed to make sure the length is a multiplier of n
    """
    while len(string) % n != 0:
        string = string + "="
    return string


def run(user_input):
    if user_input == "": user_input = input("Type the string you would like to encode and press enter.")
    print("- Encode process starting -")

    step1 = string_to_list(user_input)
    print(step1)

    step2 = code_to_ascii(step1)
    print(step2)

    step3 = ascii_to_binary(step2)
    print(step3)

    step4 = add_zero_to_binary(step3)
    print(step4)

    step5 = binary_list_to_string(step4)
    print(step5)

    step6 = string_to_strings_list(step5, 6)
    print(step6)

    step7 = add_zeros_to_string_list(step6)
    print(step7)

    step8 = binary_list_to_decimal_list(step7)
    print(step8)

    step9 = ascii_to_base_64(step8)
    print(step9)

    step10 = binary_list_to_string(step9)
    print(step10)

    final_step = fill_string_to_match_multiplier_length(step10, 4)
    print (final_step)

    print("- Encode process ended -")

    return final_step

