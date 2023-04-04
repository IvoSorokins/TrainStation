import Carriage


class TrainLinkedList(Carriage):
    counter = 0

    class Node:
        def __init__(self, carriage ):
            self.carriage = carriage
            self.next = None
            TrainLinkedList.count += 1
            self.id = f"TrainLinkedList-{TrainLinkedList.count - 1}"


