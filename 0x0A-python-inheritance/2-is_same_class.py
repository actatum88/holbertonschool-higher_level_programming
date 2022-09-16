#!/usr/bin/python3
""" Task 2 Exact same object Module"""


def is_same_class(obj, a_class):
    """ 
        Returns True if the object is exactly an instance of
        the specified class; otherwise False
    """
    return True if type(obj) is a_class else False
