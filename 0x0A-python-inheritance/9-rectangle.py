#!/usr/bin/python3
""" Task 9 Rectangle module """


Geometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(Geometry):
    """ Rectangle class addition to the BaseGeometry module """
    def __init__(self, width, height):
        """ Initializer for rectangle class """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Finds area """
        return self.__width * self.__height

    def __str__(self):
        """ Representation of the rectangle """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)