#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Construct a new Rectangle instance """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width of the rectangle """
        self.ValidateTheNumericalValue("width", value, False)
        self.__width = value

    @property
    def height(self):
        """ Return the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height of the rectangle """
        self.ValidateTheNumericalValue("height", value, False)
        self.__height = value

    @property
    def x(self):
        """ Return the x coordinate of the rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        """ Set the x coordinate of the rectangle """
        self.ValidateTheNumericalValue("x", value)
        self.__x = value

    @property
    def y(self):
        """ Return the y coordinate of the rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        """ Set the y coordinate of the rectangle """
        self.ValidateTheNumericalValue("y", value)
        self.__y = value

    def ValidateTheNumericalValue(self, attribute, value, positive_only=True):
        """
        Validate the numerical value for a given property of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attribute))
        if positive_only and value < 0:
            raise ValueError("{} must be >= 0".format(attribute))
        elif not positive_only and value <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    def area(self):
        """ Return the area of the rectangle """
        return self.width * self.height

    def display(self):
        """ Print the rectangle using the `#` character """
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """ Return the print() and str() representation of the Rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """
        if args and len(args) != 0:
            arg_idx = 0
            for arg in args:
                if arg_idx == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif arg_idx == 1:
                    self.width = arg
                elif arg_idx == 2:
                    self.height = arg
                elif arg_idx == 3:
                    self.x = arg
                elif arg_idx == 4:
                    self.y = arg
                arg_idx = arg_idx + 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        '''Returns dictionary representation of this class.'''
        return {"x": self.__x, "y": self.__y, "id": self.id,
                "height": self.__height, "width": self.__width}
