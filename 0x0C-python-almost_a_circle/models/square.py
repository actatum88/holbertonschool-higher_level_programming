#!/usr/bin/python3
""" Square module """


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    defines class Square; inherits from class Rectangle
    
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Getter size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter size """
        self.width = value
        self.height = value

    def __str__(self):
        """Prints Square"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y,
            self.size)

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
                    self.size = value
                elif key == 2:
                    self.x = value
                else:
                    self.y = value
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                if k == "size":
                    self.size = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return dictionary representation"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }