class Carriage:
    """A class representing a carriage."""
    def __init__(self, tare, length, volume=0):
        """
        Initialize Carriage object with tare, length and volume.

        Args:
            tare (int): The weight of an empty carriage.
            length (float): The length of a carriage.
            volume (float, optional): The volume of a carriage. Defaults to 0.
        """
        self.tare = tare
        self.length = length
        self.volume = volume

    def set_volume(self, volume):
        """
        Set the volume of a carriage.

        Args:
            volume (float): The volume of a carriage.
        """
        if volume > 0:
            self.volume = volume
        else:
            raise ValueError("\nWrong value! Using default volume value of 0!")
