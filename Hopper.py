from Carriage import Carriage
from Granular import Granular


class Hopper(Carriage):
    valid_cargo_types = [Granular.GRAIN.value, Granular.SAND.value, Granular.FERTILIZER.value]
    hp_counter = 0

    def __init__(self, tare, length, volume=0, cargo_type=Granular.GRAIN.value):
        super().__init__(tare, length, volume)
        self.hp = f"HP-{Hopper.hp_counter}"
        Hopper.hp_counter += 1
        self.cargo_type = cargo_type
        self.cargo_weight = 0

    def set_cargo_type(self, cargo_type):
        if self.cargo_type in Hopper.valid_cargo_types:
            self.cargo_type = cargo_type
        else:
            print("\nInvalid cargo type! \nUsing default cargo type - Grain!")

    def add_cargo(self, cargo_type, cargo_weight):
        if cargo_type in Hopper.valid_cargo_types:
            self.cargo_type = cargo_type
            self.cargo_weight = cargo_weight
        else:
            print("\nInvalid cargo type! \nUsing default cargo type - Grain!")

        # Method that returns string that represents object
    def __repr__(self):
        return f"[Hopper] ID:{self.hp} Cargo type: {self.cargo_type} Volume:{self.volume}"
