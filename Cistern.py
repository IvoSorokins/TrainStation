import Carriage


class Cistern(Carriage):     # Create a class called Cistern which will represent a cistern carriage.
    valid_cargo_types = ["Oil", "Milk", "Water"]
    ct_counter = 0

    def __init__(self, tare, length, volume, cargo_type="Oil"):
        super().__init__(tare, length, volume)
        Cistern.ct_counter += 1
        self.ct = f"CT-{Cistern.ct_counter}"
        self.cargo_type = cargo_type
        self.cargo_weight = 0

    def set_cargo_type(self, cargo_type):
        if self.cargo_type in Cistern.valid_cargo_types:
            self.cargo_type = cargo_type
        else:
            print("\nInvalid cargo type! \nUsing default cargo type - Oil!")

    def add_cargo(self, cargo_type, cargo_weight):
        if cargo_type in Cistern.valid_cargo_types:
            self.cargo_type = cargo_type
            self.cargo_weight = cargo_weight
        else:
            print("\nInvalid cargo type! \nUsing default cargo type - oil!")

        # Method that returns string that represents object
    def __repr__(self):
        return f"[Cistern] ID:{self.ct} Cargo type: {self.cargo_type} Volume:{self.volume}"
