import Carriage


class Hopper(Carriage):
    valid_cargo_types = ["Grain", "Sand", "Fertilizer"]
    hp_counter = 0

    def __init__(self, tare, length, volume, cargo_type="Grain"):
        super().__init__(tare, length, volume)
        Hopper.hp_counter += 1
        self.hp = f"HP-{Hopper.hp_counter}"
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
