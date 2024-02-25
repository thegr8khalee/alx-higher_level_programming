#!/usr/bin/python3
"""
documented
"""
import json


class Base:
    """
    documented
    lorem dcwc fa s
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        documented
        sadc cqerv qec efv
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """_summary_

        Args:
            list_dictionaries (_type_): _description_
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
