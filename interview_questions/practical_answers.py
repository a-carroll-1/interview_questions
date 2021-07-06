"""
Practical questions assessing basic python competency
"""


def string_to_int(whole_number_string):
    """
    Given a real whole number as a string, return an integer.
    Args:
        whole_number_string:

    Returns:
        integer
    """
    return int(whole_number_string)


def string_list_to_int(list_of_strings):
    """
    Given a list of real whole numbers as strings,
    return a list of equivalent integers.
    Args:
        list_of_strings:

    Returns:

    """
    return [int(x) for x in list_of_strings]


def name_case_modifier(lowercase_name):
    """
    Given a name as a lower case strings, return a
    modified string that capitalizes the name appropriately.
    Args:
        lowercase_name:

    Returns:

    """
    return lowercase_name.title()


def sorted_values(unsorted_dict):
    """
    Given an un-nested dictionary of simple key-value pairs,
    return a list containing all values as strings alphabetical.
    Args:
        unsorted_dict:

    Returns:

    """
    return sorted(unsorted_dict.values())


#
def given_value(un_nested_dict):
    """
    Given an un-nested dictionary, return the value associated
    with key 'alpha'
    Args:
        un_nested_dict:

    Returns:

    """
    return un_nested_dict['alpha']
