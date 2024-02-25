#!/usr/bin/python3
from models.base import Base

"""
documented
"""


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
