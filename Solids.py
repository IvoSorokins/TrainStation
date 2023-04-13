from enum import Enum


class Solids(Enum):
    """
    An enumeration class that defines types of Solids.

    Attributes:
    - PAPER (str): the type of paper that can be carried
    - FOOD (str): the type of food that can be carried
    - METAL_ORE (str): the type of metal ore that can be carried
    - WOOD (str): the type of wood that can be carried
    - METAL_PIPES (str): the type of metal pipes that can be carried
    - SHIPPING_CONTAINER (str): the type of shipping container that can be carried
    """
    PAPER = "Paper"
    FOOD = "Food"
    METAL_ORE = "Metal ore"
    WOOD = "Wood"
    METAL_PIPES = "Metal pipes"
    SHIPPING_CONTAINER = "Shipping container"

    @classmethod
    def as_list(cls):
        """
        Returns a list of all the values in the Solid enumeration class.

        Returns:
        - list: a list of all the values in the enumeration class
        """
        return [c.value for c in cls]
