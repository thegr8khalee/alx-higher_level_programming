#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """Representation of a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with provided width and height"""
        self._validate_dimension(width, "width")
        self._validate_dimension(height, "height")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Prints a message when an instance has been deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the private instance attribute width"""
        self._validate_dimension(value, "width")
        self.__width = value

    @property
    def height(self):
        """Getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the private instance attribute height"""
        self._validate_dimension(value, "height")
        self.__height = value

    @staticmethod
    def _validate_dimension(value, dimension_name):
        """Validates the dimension value"""
        if not isinstance(value, int):
            raise TypeError(f"{dimension_name} must be an integer")
        if value < 0:
            raise ValueError(f"{dimension_name} must be >= 0")

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a printable string representation of the rectangle"""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Returns a string representation of the rectangle for reproduction"""
        return f"Rectangle({self.__width}, {self.__height})"
