#!/usr/bin/python3
""" Module 10 student. """


class Student:
    """ Creating a class. """

    def __init__(self, first_name, last_name, age):
        """ Initializes the student class.  """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Dictionary  of student class. """
        my_dict = dict()
        