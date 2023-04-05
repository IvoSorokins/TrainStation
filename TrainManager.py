import TrainLinkedList


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
