from enum import Enum


class Solids(Enum):
    PAPER = "Paper"
    FOOD = "Food"
    METAL_ORE = "Metal ore"
    WOOD = "Wood"
    METAL_PIPES = "Metal pipes"
    SHIPPING_CONTAINER = "Shipping container"

    @classmethod  # Class method that returns a list of all the values in the enumeration class
    def as_list(cls):  # cls refers to the enumeration class itself
        return [c.value for c in cls]  # iterates over  all the instances of enum class
