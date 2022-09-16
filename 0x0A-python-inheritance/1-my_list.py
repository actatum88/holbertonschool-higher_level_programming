#!/usr/bin/python3
""" Class MyList that inherits from list
"""


class MyList(list):
    """ Inherit from list
    """
    def __init__(self):
        """ Initializes MyList 
        """
        super().__init__()

    def print_sorted(self):
        """ Prints the list sorted(ascending)
        """
        print(sorted(self))
