#!/usr/bin/python3
""" Task 1 my list module """


class MyList(list):
    """Class that inherits from list
    """

    def print_sorted(self):
        """ Function to print the list, but sorted in ascending
        """
        print(sorted(self))