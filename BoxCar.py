from typing import List
from Carriage import Carriage
from Livestock import Livestock
from Solids import Solids


class BoxCar(Carriage):
    """A class representing a box car carriage."""

    valid_cargo_types: List[str] = [Livestock.CATTLE.value, Solids.PAPER.value, Solids.FOOD.value]
    bc_counter: int = 0

    def __init__(self, tare: int, length: int, volume: int = 0, cargo_type: str = Livestock.CATTLE.value):
        """
        Initialize a BoxCar object.

        Args:
            tare (int): The weight of the empty carriage in tons.
            length (int): The length of the carriage in meters.
            volume (int, optional): The volume of the carriage in cubic meters. Defaults to 0.
            cargo_type (str, optional): The type of cargo the carriage is carrying. Defaults to Livestock.CATTLE.value.
        """
        super().__init__(tare, length, volume)
        self.id = f"BC-{BoxCar.bc_counter}"
        BoxCar.bc_counter += 1
        self.cargo_type = cargo_type
        self.volume = volume

    @staticmethod
    def set_cargo_type(cargo_type: str) -> None:
        """
        Set the cargo type for a box car.

        Args:
            cargo_type (str): The type of cargo.

        Raises:
            ValueError: If the cargo type is not valid.
        """
        if cargo_type not in BoxCar.valid_cargo_types:
            raise ValueError(f"Invalid cargo type! Valid types are: {BoxCar.valid_cargo_types}")

    def add_cargo(self, cargo_type: str, volume: float) -> None:
        """
        Add cargo to the box car.

        Args:
            cargo_type (str): The type of cargo.
            volume (float): The volume of the cargo.

        Raises:
            ValueError: If the cargo type is not valid.
        """
        if cargo_type not in BoxCar.valid_cargo_types:
            raise ValueError(f"Invalid cargo type! Valid types are: {BoxCar.valid_cargo_types}")

        self.cargo_type = cargo_type
        self.volume = volume

    def __repr__(self) -> str:
        """
        Return a string that represents the BoxCar object.

        Returns:
            str: A string representation of the BoxCar object.
        """
        return f"[Box Car] ID:{self.id} Cargo type: {self.cargo_type} Volume:{self.volume}"
