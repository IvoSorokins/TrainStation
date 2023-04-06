from Carriage import Carriage
from Livestock import Livestock
from Solids import Solids


class BoxCar(Carriage):

    valid_cargo_types = [Livestock.CATTLE.value, Solids.PAPER.value, Solids.FOOD.value]
    bc_counter = 0

    def __init__(self, tare, length, volume=0, cargo_type=Livestock.CATTLE.value):
        super().__init__(tare, length, volume)
        self.bc = f"BC-{BoxCar.bc_counter}"
        BoxCar.bc_counter += 1
        self.cargo_type = cargo_type
        self.volume = volume

    @staticmethod
    def set_cargo_type(cargo_type):
        assert cargo_type in BoxCar.valid_cargo_types, "\nInvalid cargo type! \nUsing default cargo type - Cattle!"

    def add_cargo(self, cargo_type, volume):
        if cargo_type in BoxCar.valid_cargo_types:
            self.cargo_type = cargo_type
            self.volume = volume
        else:
            print("\nInvalid cargo type! \nUsing default cargo type - Cattle!")

    # Method that returns string that represents object
    def __repr__(self):
        return f"[Box Car] ID:{self.bc} Cargo type: {self.cargo_type} Volume:{self.volume}"
