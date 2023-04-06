import Carriage
from Granular import Granular
from Solids import Solids


class Gondola(Carriage):
    valid_cargo_types = [Granular.COAL.value, Granular.GRAVEL.value, Solids.METAL_ORE.value]
    gd_counter = 0

    def __init__(self, tare, length, volume, cargo_type=Granular.COAL.value):
        super().__init__(tare, length, volume)
        self.gd = f"HP-{Gondola.gd_counter}"
        Gondola.gd_counter += 1
        self.cargo_type = cargo_type
        self.cargo_weight = 0

    def set_cargo_type(self, cargo_type):
        if self.cargo_type in Gondola.valid_cargo_types:
            self.cargo_type = cargo_type
        else:
            print("\nInvalid cargo type! \nUsing default cargo type - Coal!")

    def add_cargo(self, cargo_type, cargo_weight):
        if cargo_type in Gondola.valid_cargo_types:
            self.cargo_type = cargo_type
            self.cargo_weight = cargo_weight
        else:
            print("\nInvalid cargo type! \nUsing default cargo type - Grain!")

        # Method that returns string that represents object
    def __repr__(self):
        return f"[Gondola] ID:{self.gd} Cargo type: {self.cargo_type} Volume:{self.volume}"
