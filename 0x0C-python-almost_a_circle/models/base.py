#!/usr/bin/python3
"""
mm
"""
class Base:
    """m"""
    __nb_objects = 0
    def __init__(self, id=None):
        """m"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects