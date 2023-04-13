from enum import Enum


class Granular(Enum):
    """
        An enumeration class that defines types of Granular..

        Attributes:
        - COAL (str): the type of coal that can be carried
        - GRAVEL (str): the type of gravel that can be carried
        - GRAIN (str): the type of grain that can be carried
        - SAND (str): the type of sand that can be carried
        - FERTILIZER (str): the type of fertilizer that cam be carried
        """
    COAL = "Coal"
    GRAVEL = "Gravel"
    GRAIN = "Grain"
    SAND = "Sand"
    FERTILIZER = "Fertilizer"

    @classmethod
    def as_list(cls):
        """
        Returns a list of all the values in the enumeration class.

        Returns:
        - list: a list of strings representing the values in the enumeration class
        """
        return [c.value for c in cls]
