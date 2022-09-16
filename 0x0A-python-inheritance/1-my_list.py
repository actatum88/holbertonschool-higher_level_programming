#!/usr/bin/python3
""" Shebang! """


class MyList(list):
    """ A class MyList that inherits from list """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """ Print list in ascending order """
        print(sorted(self))
