#!/usr/bin/python3


"""Defines a class Rectangle."""


class Rectangle:
    """Represents a Rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height + self.width) * 2

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ("")

        rect_str = []
        for i in range(self.height):
            [rect_str.append('#') for j in range(self.width)]
            if i != self.height - 1:
                rect_str.append("\n")
        return ("".join(rect_str))

    def __repr__(self):
        rect_str = "Rectangle("
        rect_str += str(self.width) + ", "
        rect_str += str(self.height) + ")"
        return rect_str

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
