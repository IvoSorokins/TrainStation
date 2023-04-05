import Carriage


class TrainLinkedList(Carriage):
    def __init__(self):
        self.number = 0   # Instead of TrainLinkedList I will use number - as counters name
        self.head = None  # Used for linked list, starts from head,head pointer to keep track of the first node
        self.tail = None  # Used for linked list, points to the last node in the list

    class Node:  #
        def __init__(self, carriage):
            self.carriage = carriage
            self.next = None  # Linked lists must set pointers for next element in list using "next" keyword
            TrainLinkedList.number += 1
            self.number = f"TrainLinkedList-{TrainLinkedList.number - 1}"  # -1 makes it start from 0

        def add_first(self, carriage):  # Create a new node with the given carriage
            new_node = TrainLinkedList.Node(carriage)
            if self.head is None:  # If the list is empty
                self.head = new_node  # Set the head to the new node
                self.tail = new_node  # set the tail to the new node
            else:
                new_node.next = self.head  # Set the new node's "next" pointer to the current head
                self.head = new_node  # Set the head to the new node

        def add_last(self, carriage):
            new_node = TrainLinkedList.Node(carriage)  # Create a new node with given carriage
            if self.tail is None:  # If the list is empty
                self.head = new_node  # Set the head to the new node
                self.tail = new_node  # Set the tail to the new node
            else:
                self.tail.next = new_node  # Set the current tail's "next" pointer to the new node
                self.tail = new_node  # Set the tail to the new node

        def add_after(self, new_carriage, after_carriage):
            new_node = TrainLinkedList.Node(new_carriage)  # Create a new node with the given new carriage
            current_node = self.head  # Start at the head of the list
            while current_node is not None:
                if current_node.carriage == after_carriage:  # If the current node's carriage matches the after carriage

                    # Set the new node's "next" pointer to the current node's "next" pointer
                    new_node.next = current_node.next

                    current_node.next = new_node  # Set the current node's "next" pointer to the new node
                    if current_node == self.tail:  # If the current node is the tail
                        self.tail = new_node  # Set the tail to the new node
                    return
                current_node = current_node.next  # Move on to the next node
                raise ValueError(
                    # If the after carriage is not found, raise an error
                    f"{after_carriage} is not found in the linked list")
