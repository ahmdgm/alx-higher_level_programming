#!/usr/bin/python3

"""Defines a base model class."""
from json import dumps as dumpsOfJson
from json import loads as loadsOfJson
import csv


class Base:
    """Base model.

    This Represents the "base" for all other classes in the project.

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(dict_list):
        """
        Convert a list of dictionaries to a JSON string.
        """
        if not dict_list:
            return "[]"
        return dumpsOfJson(dict_list)

    @classmethod
    def save_to_file(cls, entities):
        """
        Writes the JSON string of a list of
        instances to a file named after the class.
        """
        # Construct the filename from the class name
        filename = cls.__name__ + ".json"
        # Open the file in write mode
        with open(filename, 'w') as file_handle:
            # If the list of instances is empty, write an empty list
            if entities is None:
                file_handle.write("[]")
            else:
                # Convert each instance to its dictionary form
                entity_dicts = [instance.to_dictionary()
                                for instance in entities]
                # Serialize the list of dictionaries to a
                # JSON string and write to the file
                file_handle.write(Base.to_json_string(entity_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return loadsOfJson(json_string)

    @classmethod
    def create(cls, **attributes):
        """
        Instantiate an object from attribute dictionary
        """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            instance = Rectangle(1, 1)
        elif cls is Square:
            instance = Square(1)
        else:
            instance = None

        instance.update(**attributes)
        return instance

    @classmethod
    def load_from_file(cls):
        """
        Load objects from a JSON file.
        """
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, 'r') as file:
                object_dicts = cls.from_json_string(file.read())
            instances = [cls.create(**obj) for obj in object_dicts]
            return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, objects_list):
        """Export a CSV file representing a list of class instances."""

        # Attribute keys for Rectangle and Square
        rectangle_attrs = ("id", "width", "height", "x", "y")
        square_attrs = ("id", "size", "x", "y")

        # Get class name of the instances
        class_name = cls.__name__

        # Convert list of objects to list of dictionaries if not empty
        dictionaries_list = (
            [*map(lambda obj: obj.to_dictionary(), objects_list)]
            if objects_list else []
        )

        # Initialize list to hold the CSV formatted strings
        csv_data = []
        for instance_dict in dictionaries_list:
            # Extract attribute values in the correct order
            instance_values = []
            instance_keys = instance_dict.keys()
            attrs = square_attrs if class_name == "Square" else rectangle_attrs
            for attribute in attrs:
                if attribute in instance_keys:
                    instance_values.append(str(instance_dict[attribute]))
            if instance_values:
                csv_data.append(instance_values)

        # Write CSV data to a file
        csv_filename = f"{class_name}.csv"
        with open(csv_filename, "w") as csv_file:
            # Write headers and rows if there are objects
            if objects_list:
                # Write appropriate headers based on the class
                attrs = square_attrs if class_name == \
                    "Square" else rectangle_attrs
                csv_file.write(",".join(attrs) + "\n")
                # Write each instance's CSV data
                for row in csv_data:
                    csv_file.write(",".join(row) + "\n")
            else:
                # Write empty array representation if no objects
                csv_file.write("[]")

    @classmethod
    def load_from_file_csv(cls):
        """Load objects from a CSV file corresponding to the class name."""
        # Get the name of the current class
        class_identifier = cls.__name__
        try:
            # Open the CSV file with the same name as the class
            with open(f"{class_identifier}.csv", "r") as csv_file:
                # Initialize a list to hold instances
                instances_list = []
                for line in csv_file:
                    # Skip the header line that contains 'id'
                    if "id" in line:
                        continue
                    # Create an instance of the class
                    instance = cls(1)if class_identifier == "Square" else cls(
                        1, 1)
                    # Update the instance with data from the CSV line
                    instance.update(*map(int, line.split(",")))
                    # Append the instance to the list
                    instances_list.append(instance)
                # Return the list of instances
                return instances_list
        except FileNotFoundError:
            # Return an empty list if the file is not found
            return []

    @staticmethod
    def draw(shapes_a, shapes_b):
        """Render rectangles and squares using turtle module.

        This method accepts two lists containing rectangle and square
        instances respectively, assigns each a random color, and
        renders them on a turtle graphics window.

        Args:
            shapes_a: List of Rectangle instances.
            shapes_b: List of Square instances.
        """
        import turtle
        import time
        from random import randrange

        # Turtle screen color settings
        turtle.Screen().colormode(255)

        # Process each Rectangle and Square instance for drawing
        for shape in shapes_a + shapes_b:
            # Initialize turtle object for shape rendering
            drawer = turtle.Turtle()
            # Assign random color to the drawer turtle
            drawer.color((randrange(255), randrange(255), randrange(255)))
            drawer.pensize(1)  # Initialize pen size for positioning

            # Position the turtle at the shape's starting coordinates
            drawer.penup()
            drawer.setpos((
                shape.x + drawer.pos()[0], shape.y - drawer.pos()[1]))

            drawer.pensize(10)  # Set drawing pen size
            drawer.pendown()  # Begin drawing

            # Outline the shape with turtle movements
            drawer.forward(shape.width)  # Bottom edge
            drawer.left(90)  # Prepare to draw side edge
            drawer.forward(shape.height)  # Side edge
            drawer.left(90)  # Prepare to draw top edge
            drawer.forward(shape.width)  # Top edge
            drawer.left(90)  # Prepare to draw other side edge
            drawer.forward(shape.height)  # Other side edge
            drawer.left(90)  # Complete the outline
            # Shape fill (color fill not applied)
            drawer.end_fill()

        # Display the window for a brief period before exit
        time.sleep(5)
