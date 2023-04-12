from enum import Enum


class Liquid(Enum):
    OIL = "Oil"
    MILK = "Milk"
    WATER = "Water"

    @classmethod  # Class method that returns a list of all the values in the enumeration class
    def as_list(cls):  # cls refers to the enumeration class itself
        return [c.value for c in cls]  # iterates over  all the instances of enum class
