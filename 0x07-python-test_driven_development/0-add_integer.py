#!/usr/bin/python3
"""
Add two integers and typecast to integer if float

"""


def add_integer(a, b=98):
    """Returns the sum of two integers a and b,
       returns an error if a and b are not ints or floats"""

    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')

    if type(a) is float:
        a = int
    if type(b) is float:
        b = int

    return a + b