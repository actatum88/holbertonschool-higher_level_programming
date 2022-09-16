#!/usr/bin/python3
""" Task 1 my list module """


class MyList(list):
    """ Class that extends the list and sorts """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """ Prints a sorted list in ascending order """
        print(sorted(self))
