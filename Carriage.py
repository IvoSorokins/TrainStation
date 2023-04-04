class Carriage:
    def __init__(self, tare, length, volume=0):
        self.tare = tare
        self.length = length
        self.volume = volume

    def set_volume(self, input ):
        if input > 0:
            self.volume = input
        else:
            print("\nWrong value! \n Using default volume value of 0!")
