import Carriage


class TrainLinkedList(Carriage):
    number = 0

    class Node:
        def __init__(self, carriage):
            self.carriage = carriage
            self.next = None
            TrainLinkedList.number += 1
            self.id = f"TrainLinkedList-{TrainLinkedList.number - 1}"  # -1 makes it start from 0

