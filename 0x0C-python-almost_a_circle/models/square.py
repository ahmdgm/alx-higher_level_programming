#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Represent a square """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize a new Square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return a string that describes
        the square's dimensions and position
        """
        # Format the output string to display square's details
        return ("[Square] ({unique_id}) {axis_x}/{axis_y} - {dimension}"
                .format(unique_id=self.id, axis_x=self.x,
                        axis_y=self.y, dimension=self.size))

    @property
    def size(self):
        """Get/set the current size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the current size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Modify the square's properties with updated values """
        if args:
            properties = ['id', 'size', 'x', 'y']
            for idx, prop in enumerate(properties):
                if idx < len(args):
                    setattr(self, prop, args[idx])
        else:
            for property_name, property_value in kwargs.items():
                setattr(self, property_name, property_value)

    def to_dictionary(self):
        """Return a dictionary representation of the square."""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
