#!/usr/bin/python3
""" Task 11 square module """


Geometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class addition to the BaseGeometry module """
    def __init__(self, size):
        """ initializes square class """
        self.integer_validator(size, size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ representation of the square """
        return '[Square] {:d}/{:d}'.format(self.__size, self.__size)
