from Carriage import Carriage
from Granular import Granular


class Hopper(Carriage):
    """
    A class representing a hopper carriage, a type of carriage used for granular cargo such as grain, sand,
    or fertilizer.

    Attributes:
    - valid_cargo_types (list of str): a list of valid cargo types for the hopper
    - hp_counter (int): a counter to keep track of the number of hopper carriages instantiated

    Methods:
    - __init__(self, tare, length, volume=0, cargo_type=Granular.GRAIN.value): Initializes a Hopper object
    - set_cargo_type(cls, cargo_type): Sets the type of cargo that the hopper can carry
    - add_cargo(self, cargo_type, volume): Adds cargo to the hopper
    - __repr__(self): Returns a string representation of the hopper
    """
    valid_cargo_types = [Granular.GRAIN.value, Granular.SAND.value, Granular.FERTILIZER.value]
    hp_counter = 0

    def __init__(self, tare, length, volume=0, cargo_type=Granular.GRAIN.value):
        """
        Initializes a Hopper object.

        Args:
        - tare (int): the weight of the empty hopper in kg
        - length (int): the length of the hopper in meters
        - volume (int): the volume of the hopper in cubic meters
        - cargo_type (str): the type of cargo the hopper is carrying (default: Granular.GRAIN.value)
        """
        super().__init__(tare, length, volume)
        self.id = f"HP-{Hopper.hp_counter}"
        Hopper.hp_counter += 1
        self.cargo_type = cargo_type
        self.volume = volume

    @classmethod
    def set_cargo_type(cls, cargo_type):
        """
        Sets the type of cargo that the hopper can carry.

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
        Adds cargo to the hopper.

        Args:
        - cargo_type (str): the type of cargo
        - volume (int): the volume of the cargo in cubic meters

        Raises:
        - ValueError: if the cargo_type is not a valid type
        """
        if cargo_type in Hopper.valid_cargo_types:
            self.cargo_type = cargo_type
            self.volume = volume
        else:
            raise ValueError("Invalid cargo type! Valid types are: " + ", ".join(str(self.valid_cargo_types)))

        # Method that returns string that represents object
    def __repr__(self):
        """
        Returns a string representation of the hopper.

        Returns:
        - str: a string representation of the hopper
        """
        return f"[Hopper] ID:{self.id} Cargo type: {self.cargo_type} Volume:{self.volume}"
