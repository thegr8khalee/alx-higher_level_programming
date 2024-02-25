#!/usr/bin/python3
from models.base import Base
"""
documented
"""


class Rectangle(Base):
    """
    documented

    Args:
        Base (_type_): _description_
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        documented

        Args:
            width (_type_): _description_
            height (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
