import TrainLinkedList
import Carriage
import math
import json


class TrainManager:
    """
    A class representing a train manager.
    """

    def __init__(self):
        """
        Initializes a new instance of the TrainManager class.
        """
        self.train_list = []  # List to hold TrainLinkedList objects

    def add_train(self):
        """
        Adds a train object to the train list.
        """
        # Create a new TrainLinkedList object for the train
        train_linked_list = TrainLinkedList.TrainLinkedList()

        # Add the TrainLinkedList object to the train list
        self.train_list.append(train_linked_list)

    def remove_train(self, train_id):
        """
        Removes a train object from the train list.

        Parameters:
            train_id (int): The identifier of the train to remove.

        Raises:
            ValueError: If the train with the given ID is not found in the train list.
        """
        for train in self.train_list:
            if train.train_id == train_id:
                self.train_list.remove(train)
                return
        raise ValueError("Couldn't find such train in the train list!")

    def avg_mean_carriages(self):
        """
        Calculates the average mean of carriages from the train list.
        """
        if not self.train_list:
            return 0  # return 0 if there are no trains in the list

        # Calculate the total mean of carriages for all trains in the list
        total_mean_carriages = sum([train.mean_carriages() for train in self.train_list])

        # Calculate the average mean of carriages
        avg_mean_carriages = total_mean_carriages / len(self.train_list)

        return avg_mean_carriages

    def std_carriage(self):
        """
        Calculates the standard deviation for carriages from the train list.
        """
        # Get the average mean of all carriages
        mean_carriages = self.avg_mean_carriages()

        # Formula sqrt(sum((single train carriage sum - average mean of all carriages)**2) / size of train list)
        # I separated it in two parts

        # Part 1  (sum((single train carriage sum - average mean of all carriages)**2)
        sum_sq_diff = sum((train.num_carriages - mean_carriages) ** 2 for train in self.train_list)

        # Part 2 /len(train.list which is size of train list
        std_deviation = math.sqrt(sum_sq_diff / len(self.train_list))

        # Return the standard deviation
        return std_deviation

    def export_as_json(self, filename):
        """
            Exports all trains in the train list as JSON to the specified file.

            Parameters:
                filename (str): The name of the file to export to.
        """
        # Create an empty list to store train data
        trains = []

        # Iterate through each train in the train list
        for train in self.train_list:

            # Create a variable to store train data
            train_data = {
                "id": train.train_id,
                "carriages": []
            }
            # Iterate through each carriage in the train
            for carriage in train:

                # Create a variable to store carriage data
                carriage_data = {
                    "id": carriage.carriage_id,
                    "cargo_type": carriage.cargo_type,
                    "volume": carriage.volume
                }
                # Add the carriage data to the train data
                train_data["carriages"].append(carriage_data)

            # Add the train data to the list of trains
            trains.append(train_data)
        # Create a dictionary to store the output data
        output_data = {"train_list": trains}

        # Write the output data to a JSON file
        with open(filename, "w") as f:
            json.dump(output_data, f, indent=4)

    def add_trains_from_json(self, filename):
        """
        Adds train objects to the train manager from a JSON file.

        Parameters:
            filename (str): The name of the file containing the JSON data.
        """
        # Open and read the JSON file
        with open(filename, "r") as f:
            data = json.load(f)

        # Loop through each train in the file
        for train_data in data["train_list"]:
            # Create a new train linked list
            train_linked_list = TrainLinkedList(train_id=None)
            # Loop through each carriage in the train
            for carriage_data in train_data["carriages"]:
                # Extract the cart type, cargo type, and volume from the carriage data
                cart_type = carriage_data["cart_type"]
                cargo_type = carriage_data["cargo_type"]
                volume = carriage_data["volume"]
                # Add the carriage to the train linked list
                train_linked_list.add_carriage(cart_type, cargo_type, volume)
            # Add the train to the train list
            self.train_list.append(train_linked_list)
