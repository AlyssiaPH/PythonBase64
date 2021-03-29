import re
import string


# Exercice 1
def string_to_list(my_string):
    """Returns the user string as a list
    :param my_string: user specified string:
    :return a list of string:"""
    return list(my_string)


# Exercice 2
def code_to_ascii(my_codes):
    """
    Convert string to ascii
    :param my_codes:
    :return a list of ascii:
    """
    for i in range(len(my_codes)):
        my_codes[i] = ord(my_codes[i])

    return my_codes


# Exercice 3
def ascii_to_binary(ascii_list):
    """
    Convert ascii list to binary list
    :param ascii_list: a list of ascii
    :return a list of binary:
    """
    for i in range(len(ascii_list)):
        ascii_list[i] = bin(ascii_list[i]).replace("0b", "")
    return ascii_list


# Exercice 4
def add_zero_to_binary(binary_list):
    """
    Adds a 0 on the left of every binary in the list and returns them
    :param binary_list: list of binaries
    :return : list of binaries with a 0 added at the beginning
    """
    for i in range(len(binary_list)):
        binary_list[i] = str(binary_list[i]).zfill(8)
    return binary_list


# Exercice 5 & 10
def binary_list_to_string(binary_list):
    """
    Convert and return a list of binaries to a single string
    :param binary_list: list of binaries
    :return: a string of every binaries combined
    """
    return "".join(binary_list)


# Exercice 6
def string_to_strings_list(string, n):
    """
    Convert a string to a list of strings
    :param string: string to be converted
    :param n: length of each string in the list that will be returned
    :return: a list of strings of n chars until there's not enough chars (last string will be of remaining chars length)
    """
    return [string[i:i+n] for i in range(0, len(string), n)]


# Exercice 7
def add_zeros_to_string_list(string_list):
    """
    Add 2 zeros on the right side of the last string in the list
    :param string_list: list of binaries
    :return: new list of strings where the last element has two 0 added on the right side
    """
    string_list[len(string_list) - 1] = string_list[len(string_list) - 1].ljust(6, '0')
    return string_list


# Exercice 8
def binary_list_to_decimal_list(binary_list):
    """
    Convert a list of binaries to a list of decimals
    :param binary_list: a list of binaries
    :return: list of decimals
    """
    for i in range(len(binary_list)):
        binary_list[i] = int(binary_list[i], 2)
    return binary_list


# Exercice 9
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


# Exercice 10
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


if __name__ == '__main__':
    user_input = input("Entrez votre chaine de caractère : ")

    exercice1 = string_to_list(user_input)
    print(exercice1)

    exercice2 = code_to_ascii(exercice1)
    print(exercice2)

    exercice3 = ascii_to_binary(exercice2)
    print(exercice3)

    exercice4 = add_zero_to_binary(exercice3)
    print(exercice4)

    exercice5 = binary_list_to_string(exercice4)
    print(exercice5)

    exercice6 = string_to_strings_list(exercice5, 6)
    print(exercice6)

    exercice7 = add_zeros_to_string_list(exercice6)
    print(exercice7)

    exercice8 = binary_list_to_decimal_list(exercice7)
    print(exercice8)

    exercice9 = ascii_to_base_64(exercice8)
    print(exercice9)

    exercice10 = binary_list_to_string(exercice9)
    print(exercice10)

    exercice11 = fill_string_to_match_multiplier_length(exercice10, 4)
    print (exercice11)



