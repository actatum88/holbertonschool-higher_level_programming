#!/usr/bin/python3
""" Module Rectangle """


from models.base import Base


class Rectangle(Base):
    """defining rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing rectangle class"""
        super().__init__(id)

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
@property
    def width(self):
        """get width"""
        return self.__width

    @property
    def height(self):
        """get height"""
        return self.__height

    @property
    def x(self):
        """get x"""
        return self.__x

    @property
    def y(self):
        """get y"""
        return self.__y

    @width.setter
    def width(self, value):
        """setr width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """set x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """set y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """ Prints rectangle with #'s """
        if self.__width == 0 or self.__height == 0:
            return ""
        print("\n" * self.__y +
              "\n".join(" " * self.__x + "#" * self.__width
                        for rows in range(self.__height)))

    def __str__(self):
        """ Returns string representation of Rectangle """

        return (f'[Rectangle] ({self.id}) '
                f'{self.__x}/{self.__y} - '
                f'{self.__width}/{self.__height}')


    def update(self, *args, **kwargs):
        """
        If args: set attributes in this order: id, width, height, x, y
        If no args given: set attributes according to kwargs
        """
        if args:
            for key, value in enumerate(args):
                if key == 0:
                    self.id = value
                elif key == 1:
                    self.width = value
                elif key == 2:
                    self.height = value
                elif key == 3:
                    self.x = value
                else:
                    self.y = value
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                if k == "width":
                    self.width = v
                if k == "height":
                    self.height = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return dictionary representation"""
        dic = {}
        dic["id"] = self.id
        dic["width"] = self.width
        dic["height"] = self.height
        dic["x"] = self.x
        dic["y"] = self.y
        return dic