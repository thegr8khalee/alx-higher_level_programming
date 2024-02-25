#!/usr/bin/python3
"""
documented
"""
from models.base import Base


class Rectangle(Base):
    """
    documented
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        documented
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """_summary_"""
        return self.__width

    @width.setter
    def width(self, value):
        """_summary_"""
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """_summary_"""
        return self.__height

    @height.setter
    def height(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """_summary_"""
        return self.__x

    @x.setter
    def x(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        if isinstance(value, int) is False:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """_summary_"""
        return self.__y

    @y.setter
    def y(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        if isinstance(value, int) is False:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """_summary_"""
        return self.width * self.height

    def display(self):
        """_summary_"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """_summary_"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """_summary_"""
        if not kwargs:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.width = args[1]
                self.id = args[0]
            elif len(args) == 3:
                self.width = args[1]
                self.id = args[0]
                self.height = args[2]
            elif len(args) == 4:
                self.x = args[3]
                self.width = args[1]
                self.id = args[0]
                self.height = args[2]
            elif len(args) == 5:
                self.y = args[4]
                self.x = args[3]
                self.width = args[1]
                self.id = args[0]
                self.height = args[2]
        else:
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
        """_summary_"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
