#!/usr/bin/python3
""" Module that validates integers """


class BaseGeometry:
    """ Superclass meant to implement geometrical shapes """
    def area(self):
        """ raises exception """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) is not int:
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))
