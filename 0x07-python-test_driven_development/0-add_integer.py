#!/usr/bin/python3
"""A module to add two numbers"""


def add_integer(a, b=98):
    """Function that adds two numbers"""
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')

    if type(b) not in (int, float):
        raise TypeError('b must be an integer')

    a = convert_to_int(a)
    b = convert_to_int(b)
    return a + b


def convert_to_int(numb):
    """A funtion that converts other numbers to integer"""
    if type(numb) is float:
        numb = int(numb)
        return numb

    return
