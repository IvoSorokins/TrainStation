from Carriage import Carriage
from Livestock import Livestock
from Solids import Solids


class BoxCar(Carriage):

    valid_cargo_types = [Livestock.CATTLE.value, Solids.PAPER.value, Solids.FOOD.value]
    bc_counter = 0

    def __init__(self, tare, length, volume, cargo_type=Livestock.CATTLE.value):
        super().__init__(tare, length, volume)
        self.bc = f"BC-{BoxCar.bc_counter}"
        BoxCar.bc_counter += 1
        self.cargo_type = cargo_type
        self.cargo_weight = 0

    def set_cargo_type(self, cargo_type):
        if self.cargo_type in BoxCar.valid_cargo_types:
            self.cargo_type = cargo_type
        else:
            print("\nInvalid cargo type! \nUsing default cargo type - cattle!")

    def add_cargo(self, cargo_type, cargo_weight):
        if cargo_type in BoxCar.valid_cargo_types:
            self.cargo_type = cargo_type
            self.cargo_weight = cargo_weight
        else:
            print("\nInvalid cargo type! \nUsing default cargo type - cattle!")

    # Method that returns string that represents object
    def __repr__(self):
        return f"[Box Car] ID:{self.bc} Cargo type: {self.cargo_type} Volume:{self.volume}"
