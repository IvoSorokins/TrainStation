from Carriage import Carriage
from Granular import Granular
from Solids import Solids


class Gondola(Carriage):
    """
            Class representing a gondola carriage.

            Attributes:
            - tare (int): the weight of the empty gondola in kg
            - length (int): the length of the gondola in meters
            - volume (int): the volume of the gondola in cubic meters
            - cargo_type (str): the type of cargo the gondola is carrying

            Class Attributes:
            - valid_cargo_types (list): a list of valid cargo types for the gondola
            - gd_counter (int): a counter for the ID of gondolas created

            Methods:
            - set_cargo_type(cls, cargo_type): sets the type of cargo the gondola is carrying
            - add_cargo(self, cargo_type, volume): adds cargo to the gondola
            - __repr__(self): returns a string representation of the gondola
            """
    valid_cargo_types = [Granular.COAL.value, Granular.GRAVEL.value, Solids.METAL_ORE.value]
    gd_counter = 0

    def __init__(self, tare, length, volume=0, cargo_type=Granular.COAL.value):
        """
            Initializes a Gondola object.

            Args:
            - tare (int): the weight of the empty gondola in kg
            - length (int): the length of the gondola in meters
            - volume (int): the volume of the gondola in cubic meters
            - cargo_type (str): the type of cargo the gondola is carrying (default: Granular.COAL.value)
            """
        super().__init__(tare, length, volume)
        self.id = f"GD-{Gondola.gd_counter}"
        Gondola.gd_counter += 1
        self.cargo_type = cargo_type

    @classmethod
    def set_cargo_type(cls, cargo_type):
        """
        Sets the type of cargo that the gondola can carry.

        Args:
        - cargo_type (str): the type of cargo

        Raises:
        - ValueError: if the cargo_type is not a valid type
        """
        if cls.cargo_type in cls.valid_cargo_types:
            cls.cargo_type = cargo_type
        else:
            raise ValueError("Invalid cargo type! Valid types are: " + ", ".join(str(cls.valid_cargo_types)))

    def add_cargo(self, cargo_type, volume):
        """
                Adds cargo to the gondola.

                Args:
                - cargo_type (str): the type of cargo
                - volume (int): the volume of the cargo in cubic meters

                Raises:
                - ValueError: if the cargo_type is not a valid type
                """
        if cargo_type in Gondola.valid_cargo_types:
            self.cargo_type = cargo_type
            self.volume = volume
        else:
            raise ValueError("Invalid cargo type! Valid types are: " + ", ".join(str(self.valid_cargo_types)))

    def __repr__(self):
        """
                Returns a string representation of the gondola.

                Returns:
                - str: a string representation of the gondola
                """
        return f"[Gondola] ID:{self.id} Cargo type: {self.cargo_type} Volume:{self.volume}"
