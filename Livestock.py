from enum import Enum


class Livestock(Enum):
    CATTLE = "Cattle"


    @classmethod  # Class method that returns a list of all the values in the enumeration class
    def as_list(cls):  # cls refers to the enumeration class itself
        return [cls.CaTTLE.value]
