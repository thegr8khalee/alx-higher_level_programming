#!/usr/bin/python3
"""
documented
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """_summary_

    Args:
        Rectangle (_type_): _description_
    """

    def __init__(self, size, x=0, y=0, id=None):
        """_summary_

        Args:
            size (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """_summary_"""
        if not kwargs:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.size = args[1]
                self.id = args[0]
            elif len(args) == 3:
                self.size = args[1]
                self.id = args[0]
                self.x = args[2]
            elif len(args) == 4:
                self.y = args[3]
                self.size = args[1]
                self.id = args[0]
                self.x = args[2]
        else:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
