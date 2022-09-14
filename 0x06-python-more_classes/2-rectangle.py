#!/usr/bin/python3
""" Defines a rectangle class"""


class Rectangle:
    """ Class that defines a rectangle """
    def __init__(self, width=0, height=0):
        """ Initializes a new rectangle.
        Arguments:
                  width (int): width of new rectangle
                  height (int): height of new rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Gets and sets the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ Gets and sets the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height * self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

        def __str__(self):
        if self.perimeter() == 0:
            return ""
        row = '#' * self.__width
        square = ""
        for i in range(self.height):
            if i < (self.__height - 1):
                square += row + '\n'
            if i == (self.__height - 1):
                square += row
        return square
        