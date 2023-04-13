from enum import Enum


class Liquid(Enum):
    """
    An enumeration class that defines types of liquids that can be carried by a tank.

    Attributes:
    - OIL (str): the type of oil that can be carried
    - MILK (str): the type of milk that can be carried
    - WATER (str): the type of water that can be carried
    """

    OIL = "Oil"
    MILK = "Milk"
    WATER = "Water"

    @classmethod
    def as_list(cls):
        """
        Returns a list of all the values in the enumeration class.

        Returns:
        - List[str]: a list of all the values in the enumeration class
        """
        return [c.value for c in cls]
