from enum import Enum


class Granular(Enum):
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
