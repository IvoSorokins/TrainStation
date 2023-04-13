from Carriage import Carriage
from Liquid import Liquid


class Cistern(Carriage):
    """
        Class representing a cistern carriage.

        Attributes:
        - tare (int): the weight of the empty carriage in kg
        - length (int): the length of the carriage in meters
        - volume (int): the volume of the carriage in cubic meters
        - cargo_type (str): the type of cargo the cistern is carrying

        Class Attributes:
        - valid_cargo_types (list): a list of valid cargo types for the cistern
        - cistern_counter (int): a counter for the ID of cisterns created

        Methods:
        - set_cargo_type(cls, cargo_type): sets the type of cargo the cistern is carrying
        - add_cargo(cls, cargo_type, volume): adds cargo to the cistern
        - __repr__(self): returns a string representation of the cistern
        """
    valid_cargo_types = [Liquid.OIL.value, Liquid.MILK.value, Liquid.WATER.value]
    cistern_counter = 0

    def __init__(self, tare, length, volume=0, cargo_type=Liquid.OIL.value):
        """
        Initializes a Cistern object.

        Args:
        - tare (int): the weight of the empty carriage in kg
        - length (int): the length of the carriage in meters
        - volume (int): the volume of the carriage in cubic meters
        - cargo_type (str): the type of cargo the cistern is carrying (default: Liquid.OIL.value)
        """
        super().__init__(tare, length, volume)
        self.id = f"CT-{Cistern.cistern_counter}"
        Cistern.cistern_counter += 1
        self.cargo_type = cargo_type

    @classmethod
    def set_cargo_type(cls, cargo_type):
        """
        Sets the type of cargo that the cistern can carry.

        Args:
        - cargo_type (str): the type of cargo

        Raises:
        - ValueError: if the cargo_type is not a valid type
        """
        if cargo_type in cls.valid_cargo_types:
            cls.cargo_type = cargo_type
        else:
            raise ValueError("Invalid cargo type! Valid types are: " + ", ".join(str(cls.valid_cargo_types)))

    def add_cargo(self, cargo_type, volume):
        """
        Adds cargo to the cistern.

        Args:
        - cargo_type (str): the type of cargo
        - volume (int): the volume of the cargo in cubic meters

        Raises:
        - ValueError: if the cargo_type is not a valid type
        """
        if cargo_type in self.valid_cargo_types:
            self.cargo_type = cargo_type
            self.volume = volume
        else:
            raise ValueError("Invalid cargo type! Valid types are: " + ", ".join(str(self.valid_cargo_types))

    def __repr__(self):
        """
        Returns a string representation of the cistern.

        Returns:
        - str: a string representation of the cistern
        """
        return f"[Cistern] ID:{self.id} Cargo type: {self.cargo_type} Volume:{self.volume}"
