from Carriage import Carriage
from Liquid import Liquid


class Cistern(Carriage):     # Create a class called Cistern which will represent a cistern carriage.
    valid_cargo_types = [Liquid.OIL.value, Liquid.MILK.value, Liquid.WATER.value]
    ct_counter = 0

    def __init__(self, tare, length, volume=0, cargo_type=Liquid.OIL.value):
        super().__init__(tare, length, volume)
        self.id = f"CT-{Cistern.ct_counter}"
        Cistern.ct_counter += 1
        self.cargo_type = cargo_type
        self.volume = volume

    def set_cargo_type(self, cargo_type):
        if self.cargo_type in Cistern.valid_cargo_types:
            self.cargo_type = cargo_type
        else:
            print("\nInvalid cargo type! \nUsing default cargo type - Oil!")

    def add_cargo(self, cargo_type, volume):
        if cargo_type in Cistern.valid_cargo_types:
            self.cargo_type = cargo_type
            self.volume = volume
        else:
            print("\nInvalid cargo type! \nUsing default cargo type - Oil!")

        # Method that returns string that represents object
    def __repr__(self):
        return f"[Cistern] ID:{self.id} Cargo type: {self.cargo_type} Volume:{self.volume}"
