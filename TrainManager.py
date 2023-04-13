from TrainLinkedList import TrainLinkedList
from BoxCar import BoxCar
from Hopper import Hopper
from Cistern import Cistern
from Gondola import Gondola

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

    def add_train(self, train):
        """
        Adds a train object to the train list.

        Parameters:
            train (TrainLinkedList): The train object to add to the train list.
        """

        # Add the TrainLinkedList object to the train list
        self.train_list.append(train)

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

        Returns:
            float: The average mean of carriages.
        """
        if not self.train_list:
            return 0  # return 0 if there are no trains in the list

        # Calculate the total number of carriages for all trains in the list
        total_carriage_count = sum([train.get_carriage_count() for train in self.train_list])

        # Calculate the average mean of carriages
        avg_mean_carriages = total_carriage_count / len(self.train_list)

        return avg_mean_carriages

    def std_carriage(self, train):
        """
        Calculates the standard deviation for carriages from the train list.

        Parameters:
            train (TrainLinkedList): The train object to calculate the standard deviation for.

        Returns:
            float: The standard deviation for carriages.
        """
        train_count = 0
        for train in self.train_list:
            train_count += 1
        std = math.sqrt((float((float(train.get_carriage_count()) -
                                (float(self.avg_mean_carriages())))**2 / train_count)))
        return std

    def export_as_json(self, file_name):
        """
        Exports the train list as a JSON file.

        Parameters:
        file_name (str): The name of the file to export the JSON data to.
        """
        train_data = []
        for train in self.train_list:
            train_id = train.train_id
            carriage_data = []
            current_node = train.head
            while current_node:
                carriage_id = current_node.carriage.id
                cargo_type = current_node.carriage.cargo_type
                volume = current_node.carriage.volume
                carriage_data.append({
                    "id": carriage_id,
                    "cargo_type": cargo_type,
                    "volume": volume
                })
                current_node = current_node.next
            train_data.append({
                "id": train_id,
                "carriages": carriage_data
            })
        output_data = {"train_list": train_data}
        with open(file_name, "w") as output_file:
            json.dump(output_data, output_file, indent=2)

    def add_trains_from_json(self, file_path):
        """
        Adds trains from a JSON file to the train list.

        Parameters:
        fil_path (str): The path to the JSON
        """
        with open(file_path) as f:
            data = json.load(f)
            for train_data in data['train_list']:
                train = TrainLinkedList()
                for carriage_data in train_data['carriages']:
                    if "HP-" in carriage_data['id']:
                        carriage = Hopper(carriage_data['cargo_type'], carriage_data['volume'])
                    elif "BC-" in carriage_data['id']:
                        carriage = BoxCar(carriage_data['cargo_type'], carriage_data['volume'])
                    elif "CT-" in carriage_data['id']:
                        carriage = Cistern(carriage_data['cargo_type'], carriage_data['volume'])
                    elif "GD-" in carriage_data['id']:
                        carriage = Gondola(carriage_data['cargo_type'], carriage_data['volume'])
                    else:
                        raise ValueError("Wrong ID inside add_from_json")
                    train.add_last(carriage)
                self.add_train(train)
