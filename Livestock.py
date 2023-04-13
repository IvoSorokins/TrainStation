from enum import Enum


class Livestock(Enum):
    """
        An enumeration class that defines types of livestock.

        Attributes:
        - CATTLE (str): the type of cattle that can be carried
        """
    CATTLE = "Cattle"

    @classmethod
    def as_list(cls):
        """
        Returns a list of all the values in the Livestock enumeration class.

        Returns:
        - list: a list of all the values in the enumeration class
        """
        return [cls.CATTLE.value]
