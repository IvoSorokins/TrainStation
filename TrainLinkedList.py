import Carriage


class TrainLinkedList(Carriage):
    def __init__(self):
        number = 0   # Instead of TrainLinkedList I will use number - as counters name
        self.head = None  # Used for linked list, starts from head,head pointer to keep track of the first node
        self.tail = None  # Used for linked list, points to the last node in the list

    class Node:
        def __init__(self, carriage):
            self.carriage = carriage
            self.next = None  # Linked lists must set pointers for next element in list using "next" keyword
            TrainLinkedList.number += 1
            self.number = f"TrainLinkedList-{TrainLinkedList.number - 1}"  # -1 makes it start from 0
